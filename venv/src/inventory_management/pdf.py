# pdf.py

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os

def fetch_resources(uri, rel):
    # Function to handle image inclusion in the PDF
    path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_path, context_dict):
    template = get_template(template_path)

    html = template.render(context_dict)
    result = BytesIO()

    # Pass the fetch_resources function to pisa to handle image inclusion
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding="UTF-8", link_callback=fetch_resources)
    if not pdf.err:
        return result.getvalue()
    return None
