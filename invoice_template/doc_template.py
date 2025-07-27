import os
from docxtpl import DocxTemplate
from datetime import datetime
from docx2pdf import convert


def generate_invoice_pdf(invoice_data, template_path="invoice_template/invoice_template.docx",progress_callback = None):

    if progress_callback: progress_callback(0.1)
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_docx = os.path.join(desktop_path, f"invoice_{invoice_data['customer_name']}.docx")
    output_pdf = output_docx.replace('.docx', '.pdf')


    if progress_callback: progress_callback(0.3)

    doc = DocxTemplate(template_path)

    context = {
        "customer_name": invoice_data["customer_name"],
        "customer_address": invoice_data["address"],
        "customer_mobile": invoice_data["mobile"],
        "invoice_number": invoice_data["invoice_no"],
        "date": datetime.now().strftime("%d-%m-%Y"),
        "items": invoice_data["items"],
        "gross_total": invoice_data["gross_total"],
        "total": invoice_data["total"]
    }

    doc.render(context)
    if progress_callback:progress_callback(0.6)

    doc.save(output_docx)
    if progress_callback:progress_callback(0.8)

    convert(output_docx, output_pdf)
    if progress_callback:progress_callback(1.0)

    print("Invoice PDF generated at:", output_pdf)


