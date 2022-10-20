from django.urls  import path

from .views import IndexView , DadosJASONView, ConvertPdfView  ,  CaptureAndConvertPdf

urlpatterns = [
    path( '' , IndexView.as_view()  ,  name='index'),
    path('dados' , DadosJASONView.as_view() , name='dados'),
    #path('pdf' , ConvertPdfView.as_view() , name='pdf'),
    path('capturepdf' , CaptureAndConvertPdf.as_view() , name='pdf2'),
]
