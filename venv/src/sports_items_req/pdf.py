# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# import io

# def render_to_pdf_req(template_path, context={}):
#     template = get_template(template_path)
#     html = template.render(context)
#     result = io.BytesIO()
#     pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

