from django.shortcuts import render
from  django.http import HttpResponse
from django.template.loader import  get_template
from xhtml2pdf import  pisa


def bill(request):
    template_name='bill.html'
    return render(request,template_name)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_bill(request):
    template_name = 'genbill.html'

    if request.method == 'POST':
        orange = int(request.POST['orange'])
        mango = int(request.POST['mango'])
        papaya = int(request.POST['papaya'])
        apple = int(request.POST['apple'])
        dt = request.POST['dt']

        orange_rt = 500
        mango_rt = 700
        papaya_rt = 250
        apple_rt = 500

        total = (orange * orange_rt + mango * mango_rt + papaya * papaya_rt + apple * apple_rt)
        context = {
            'orange': orange,
            'mango': mango,
            'papaya': papaya,
            'apple': apple,
            'dt': dt,
            'total': total,
        }

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="bill_Invoice.pdf"'
        # Find the template and render it.
        template = get_template(template_name)
        html = template.render(context)

        # Create a PDF
        pisa_status = pisa.CreatePDF(html, dest=response)
        # If there's an error, handle it accordingly
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + pisa_status.err + '</pre>')
        return response

    return render(request, template_name)
