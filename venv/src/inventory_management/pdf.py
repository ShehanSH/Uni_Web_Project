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


from io import BytesIO
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.db.models import Sum
from .models import Category, Inventory_Stock

def generate_category_wise_inventory_report(request):
    categories = Category.objects.all()
    inventory_stocks = Inventory_Stock.objects.all()

    # Calculate total stock quantity, damage quantity, and lost quantity for each category
    for category in categories:
        category_stocks = inventory_stocks.filter(category=category)
        category.total_stock_quantity = category_stocks.aggregate(Sum('stock_quantity'))['stock_quantity__sum']
        category.total_damage_quantity = category_stocks.aggregate(Sum('damage_quantity'))['damage_quantity__sum']
        category.total_lost_quantity = category_stocks.aggregate(Sum('lost_quantity'))['lost_quantity__sum']

    context = {
        'categories': categories,
    }

    # Render the HTML template with the data
    template = get_template('category_wise_inventory_report.html')
    html = template.render(context)

    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="category_wise_inventory_report.pdf"'

    # Generate the PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF')

    return response
