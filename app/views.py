from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
        return render(request, 'portfolio.html')

def portfolio_details(request):
        return render(request, 'portfolio-details.html')

def resume(request):
        return render(request, 'resume.html')

def services(request):
        return render(request, 'services.html')

def service_details(request):
        return render(request, 'service-details.html')

def starter_page(request):
        return render(request, 'starter-page.html')
