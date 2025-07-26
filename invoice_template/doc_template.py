from docxtpl import DocxTemplate
from datetime import datetime
from docx2pdf import convert


def generate_invoice_pdf(invoice_data, template_path="invoice_template/invoice_template.docx",
                         output_path="invoice_output.docx"):
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
    doc.save(output_path)

    output_pdf = output_path.replace(".docx", ".pdf")
    convert(output_path, output_pdf)

    print("Invoice PDF generated at:", output_pdf)


