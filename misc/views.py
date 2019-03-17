from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactUsForm

# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
          name = form['name']
          message = form['message']
          from_email = form['email']
          to_email = 'cyphercreedcommunity@gmail.com'
          send_mail(
            'ContactUs Mail by '+ str(name),
            message,
            from_email,
            (to_email,),
        )  
    else:
        form = ContactUsForm()
    return render(request,'misc/contact_us.html',{'form':form})

# def contact_us(request):
#     if request.method == 'POST':
#         name = request['name']
#         email = request['email']
#         message = request['message']
#         send_mail(
#             'ContactUs Mail by '+name,
#             message,
#             email,
#             ['cyphercreedcommunity@gmail.com'],
#             fail_silently=False
#         )
#     return redirect('homepage')