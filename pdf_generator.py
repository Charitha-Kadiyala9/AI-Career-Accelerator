from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_resume_pdf(resume_content):

    filename = "Resume.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Resume",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    for line in resume_content.split("\n"):

        if line.strip():

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 4)
            )

    doc.build(content)

    return filename


def create_cover_letter_pdf(cover_content):

    filename = "Cover_Letter.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Cover Letter",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    for line in cover_content.split("\n"):

        if line.strip():

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 4)
            )

    doc.build(content)

    return filename