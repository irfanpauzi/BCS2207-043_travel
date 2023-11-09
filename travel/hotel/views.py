from django.shortcuts import render
from hotel.models import Review

# Create your views here.
def index(request):
    return render(request,'index.html')

def review(request):
    if request.method == 'POST':
        name = request.POST['name']
        text= request.POST['text']
        data = Review(name=name,text=text)
        data.save()

    data=Review.objects.all()
    dict = {
        'allreview': data
    }
    return render(request,'review.html',dict)
