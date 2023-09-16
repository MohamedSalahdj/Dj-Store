from .models import Company

def get_company_info(request):
    data = Company.objects.last()
    context = {
        'company':data
    }
    return context