import os
import sys
import shutil
import tempfile
from docxtpl import DocxTemplate
from datetime import datetime
from pathlib import Path

try:
    from docx2pdf import convert
except ImportError:
    convert = None  # fallback if not available


def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and PyInstaller exe) """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def generate_invoice_pdf(invoice_data, template_path="invoice_template/invoice_template.docx", progress_callback=None):
    if progress_callback:
        progress_callback(0.1)

    # ✅ Copy template to temp (Word/docx2pdf needs writable file)
    resolved_template = resource_path(template_path)
    temp_dir = Path(tempfile.gettempdir())
    temp_template = temp_dir / "invoice_template.docx"
    shutil.copy(resolved_template, temp_template)

    # Save invoices to Desktop/Invoices
    desktop_path = Path.home() / "Desktop"
    invoice_path = desktop_path / "Invoices"
    invoice_path.mkdir(parents=True, exist_ok=True)

    output_docx = invoice_path / f"invoice_{invoice_data['customer_name']}.docx"
    output_pdf = str(output_docx).replace(".docx", ".pdf")

    if progress_callback:
        progress_callback(0.3)

    # Render template
    doc = DocxTemplate(temp_template)
    context = {
        "customer_name": invoice_data["customer_name"],
        "customer_address": invoice_data["address"],
        "customer_mobile": invoice_data["mobile"],
        "customer_gst": invoice_data.get("customer_gst", ""),
        "invoice_number": invoice_data["invoice_no"],
        "date": datetime.now().strftime("%d-%m-%Y"),
        "items": invoice_data["items"],
        "gross_total": float(round(invoice_data["gross_total"], 2)),
        "total": float(round(invoice_data["total"], 2)),
    }
    doc.render(context)

    if progress_callback:
        progress_callback(0.6)

    # Save DOCX
    doc.save(output_docx)

    if progress_callback:
        progress_callback(0.8)

    # ✅ Convert DOCX → PDF if possible
    pdf_generated = False
    if convert:
        try:
            convert(output_docx, output_pdf)
            pdf_generated = True
        except Exception as e:
            print(f"⚠️ PDF conversion failed: {e}")
    else:
        print("⚠️ docx2pdf not available, skipping PDF conversion")

    if progress_callback:
        progress_callback(1.0)

    print("✅ Invoice generated:")
    print("   DOCX:", output_docx)
    if pdf_generated:
        print("   PDF :", output_pdf)
    else:
        print("⚠️ PDF not created (Word may not be installed).")

    # ✅ Always return both paths
    return (str(output_pdf) if pdf_generated else None), str(output_docx)
