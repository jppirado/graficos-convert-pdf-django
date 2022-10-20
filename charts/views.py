

from django.shortcuts import render

# Create your views here.

from random import randint 
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJASONView(BaseLineChartView):
    
    def get_labels(self):
        #coluna
        return [
            'jan','fev','mar','abr','mai','jun','jul','aug','sep','out' , 'nov', 'dez'
        ] 
    
    def get_providers(self):
        #linha
        datasets = [
            'teste 1',
            'teste 2',
            'teste 3',
        ]

        return datasets

    def get_data(self): 
        dados = []

        for c in  range(3):
            for l in range(12):
                dado= [
                    randint(1,200),
                    randint(1,200) ,
                    randint(1,200),
                    randint(1,200),
                    randint(1,200) ,
                    randint(1,200) ,
                    randint(1,200),
                    randint(1,200) ,
                    randint(1,200),
                    randint(1,200),
                    randint(1,200) ,
                    randint(1,200),
                ]
            dados.append(dado)

        return dados  

import io 
from django.views.generic import View
from django.http import FileResponse      
import os 
os.add_dll_directory("C:\Program Files\GTK3-Runtime Win64\bin")
from reportlab.pdfgen  import canvas

class ConvertPdfView( View ):

    def get( self , request , *args, **kwargs ):

        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)

        pdf.drawString(100,100, 'JPLINDADASD KASLÇD')
        pdf.showPage()
        pdf.save()

        buffer.seek(0)

        #return FileResponse(buffer,  as_attachment = True , filename='relatorio1.pdf')
        return FileResponse(buffer, filename="relatioaisosa.pdf" )

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse 
from weasyprint import HTML

class CaptureAndConvertPdf(view):
    def get(self, request, *args, **kwargs ):
        
        txt = ['i','o']

        html_string = render_to_string( 'intex.html' , { 'txt' : txt  } )
        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')

        fs = FileSystemStorage('/tmp/')

        with fs.open('relatorio2.pdf') as pdf :
            response  = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'
            return response 