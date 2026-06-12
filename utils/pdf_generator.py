from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    revenue,
    profit,
    margin,
    total_customers,
    top_product,
    top_segment
):

    filename = "executive_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Multi-Agent Business Intelligence Platform",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 20))

    report = f"""
    <b>Executive Report</b><br/><br/>

    Revenue: ${revenue:,.2f}<br/>
    Profit: ${profit:,.2f}<br/>
    Profit Margin: {margin:.2f}%<br/>
    Total Customers: {total_customers}<br/><br/>

    Top Customer Segment:
    {top_segment}<br/><br/>

    Top Revenue Product:
    {top_product}
    """

    content.append(
        Paragraph(
            report,
            styles["BodyText"]
        )
    )

    doc.build(content)

    return filename