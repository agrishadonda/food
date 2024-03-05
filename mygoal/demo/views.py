from django.shortcuts import render,redirect
from django.views import View
from .models import banner,blog1
from .form import HotelForm,date,email,MyForm,PersonForm
# Create your views here.
class hotel(View):
    
    hotel5 = banner.objects.all()
    def get(self,request,*args,**kwargs):
        form1=email()
        form2 = date()
        form3 = PersonForm()
        data = {
            'person_form':form3,
           'email_form':form1, 
            'date_form':form2,
            'rec5':self.hotel5
        }
        return render(request,'hotel.html',data)
    def post(self,request,*args, **kwargs):
            form = HotelForm(request.POST)
            form1 = email(request.Post)
            form2 = date(request.Post)
            form3 = PersonForm(request.POST)
            if form.is_valid():
                form.save()
            elif form1.is_valid():
                  form1.save()
            elif form2.is_valid():
                  form2.save()
            elif form3.is_valid():
                  form3.save()
            return redirect('hotel')
        
class about(View):
    hotel5 = banner.objects.all()
    def get(self,request,*args, **kwargs):
        form1 = email()
        form2 = date()
        form3 = PersonForm()
        data = {
            'person_form':form3,
            'email_form':form1,
            'date_form':form2,
            'rec5':self.hotel5
        }
        
        return render(request,'about.html',data)
class menu(View):
    def get(self,request,*args, **kwargs):
        return render(request,'menu.html')
class blog(View):
    hotel1 = blog1.objects.all()    
    def get(self,request,*args, **kwargs):
        data = {
            'recs1':self.hotel1,
            }
        return render(request,'blog.html',data)
class contact(View):
    
    def get(self,request,*args, **kwargs):
        form=HotelForm()
        return render(request,'contact.html',{'form':form})
    
def form(request):
    data = MyForm()
    return render(request,'form.html',{'form':data})

   




    