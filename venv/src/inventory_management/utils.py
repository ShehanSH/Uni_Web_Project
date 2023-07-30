# # utils.py

# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML

# def generate_pdf_response(template_name, context=None, filename=None):
#     """
#     Generate a PDF response from an HTML template using WeasyPrint.

#     Parameters:
#         template_name (str): The name of the HTML template to render.
#         context (dict, optional): The context data to pass to the template. Default is None.
#         filename (str, optional): The filename to use for the downloaded PDF. Default is None.

#     Returns:
#         HttpResponse: A PDF response that can be directly downloaded.
#     """
#     if context is None:
#         context = {}

#     html_string = render_to_string(template_name, context)
#     pdf_file = HTML(string=html_string).write_pdf()

#     response = HttpResponse(content_type='application/pdf')
#     if filename:
#         response['Content-Disposition'] = f'attachment; filename="{filename}.pdf"'
#     else:
#         response['Content-Disposition'] = 'attachment; filename="document.pdf"'

#     response.write(pdf_file)
#     return response
