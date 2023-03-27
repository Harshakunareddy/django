from django.shortcuts import render

# Create your views here.
def demo(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        image=request.FILES.get['image']
        k=Contact(name=name,email=email,message=message,image=image)
        k.save()
    return render(request,'base.html')