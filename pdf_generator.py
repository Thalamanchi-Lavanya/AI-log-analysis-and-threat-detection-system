import sqlite3

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf():

    pdf = SimpleDocTemplate(
        "reports/Threat_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "AI Threat Detection Report",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 20))

    connection = sqlite3.connect(
        "database/threats.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM threats"
    )

    threats = cursor.fetchall()

    connection.close()

    total = len(threats)

    content.append(
        Paragraph(
            f"Total Threats Detected: {total}",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 15))

    for threat in threats:

        text = (
            f"ID: {threat[0]} | "
            f"User: {threat[1]} | "
            f"Attack: {threat[2]} | "
            f"Risk: {threat[3]}"
        )

        content.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 5)
        )

    pdf.build(content)

    print("PDF Report Generated Successfully")