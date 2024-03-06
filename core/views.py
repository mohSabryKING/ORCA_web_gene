from django.shortcuts import *
from .form import *
from django.views.generic.base import * 
from django.views.generic import *
from .Gene import *

# Create your views here.
class Home_page(TemplateView):
      template_name="home.html"
      def get_context_data(self, **kwargs):
          context = super(Home_page, self).get_context_data(**kwargs)
          serv_list=[]
          for i in range(9):
              context['serv_'+str(i)]=Serv[i][0]
              serv_list.insert(i,context['serv_'+str(i)])
          '''context['serv_1']=Serv[0][1]
          context['serv_2']=Serv[1][1]
          context['serv_3']=Serv[2][1]
          context['serv_4']=Serv[3][1]
          context['serv_5']=Serv[4][1]
          context['serv_6']=Serv[5][1]
          context['serv_7']=Serv[6][1]
          context['serv_8']=Serv[7][1]
          
          context['serv_8']=Serv[8][1]
          
          context['serv_8']=Serv[9][1]
          
          raw data 
          
          
          
          print("3 Models displayed")
          print("=="*30)
          context['all_offers']=[Service_offers.objects.create(pk=i) for i in range(20)]
          context['all_proj']=[Projects.objects.create(pk=i) for i in range(30)]
          context['all_emps']=[Employee_model.objects.create(pk=i) for i in range(40)]
          print("=="*30)
          
          '''
          print("adjusted lists ")
          print("->"*10)
          print(serv_list)
          context['serv_all']=serv_list
          context['all_emp']=all_emps[:4]
          context['offers']=all_offers[:3]
          context['all_proj']=all_proj[:5]
          print("->"*10)
        
          
          return context




class Register_form(CreateView):
     template_name='registration/add_user.html'
     form_class=Add_user
     success_url='/user_added/'
     def is_valid(self):
         valid = super().is_valid()
         if not valid:
             return False
         # Custom Logic
         return redirect('your_country')

#for the projects
#===================================================================
class Proj_sectors(TemplateView):
         
        template_name='proj/proj_type.html'
        def get_context_data(self, **kwargs):
            context = super(Proj_sectors, self).get_context_data(**kwargs)
            serv_list=[]
            print("project sectors")
            for i in range(9):
              context['serv_'+str(i)]=Serv[i][0]
              serv_list.insert(i,context['serv_'+str(i)])
            context['proj_sec']=make_list(Serv)
            context['serv_all']=serv_list
            return context



class Proj_List(ListView):
         model = Projects
         context_object_name = 'proj_all'
         template_name='proj/proj_list.html'

def proj_data(h,type_x):
     projects_of=Projects.objects.filter(proj_type=type_x)
     serv_list=[]
     if type_x:
       print(type_x)
       print(projects_of)
     for i in range(9):
              serv_list.insert(i,Serv[i][0])
     return render(h,'proj/proj_all.html',{'proj_x':projects_of,'serv_all':serv_list})


def proj_item(h,type_x,p):
     project_x=Projects.objects.filter(proj_type=type_x,id=p)
     project_y=Projects.objects.get(id=p)
     print(type_x)
     return render(h,'proj/proj_item.html',{'proj_x':project_x,'proj_y':project_y,})
#===================================================================






#for the SERVICES
#===================================================================
class Select_service(TemplateView):
     template_name='serv/services.html'
     def get_context_data(self, **kwargs):
         context = super(Select_service, self).get_context_data(**kwargs)
         context['serv_list']=make_list(Serv)
         print(context['serv_list'])
         return context
     

class Select_service_offers(TemplateView):
    template_name='serv/serv_offers.html'
    def get_context_data(self, **kwargs):
        s_type=kwargs.pop('o')
        context = super(Select_service_offers, self).get_context_data(**kwargs)
        print("selected service :",s_type)
        context['x_offers']=Service_offers.objects.filter(serv_offer=s_type)
        context['s']=make_list(Serv)
        print(context['x_offers'])
        return context



def offer_item(h,o,id):
    offer_x=Service_offers.objects.filter(serv_offer=o,pk=id)
    print(offer_x)     
    return render(h,'serv/offer_item.html')

#===================================================================



#for the Employee
#===================================================================
def employee_type_list(h):
     print(make_list(Job))
     return render(h,'emp/emp_type.html',{'e_type':make_list(Job)})
def emp_list(h,e_type):
     emp_x=Employee_model.objects.filter(job=e_type)
     emp_type=make_list(Job)
     return render(h,'emp/emp_list.html',{'emp_x':emp_x,'emp_type':emp_type})

def emp_item(h,e_type,e_id):
    return render(h,'emp/emp_profile.html')
#===================================================================








class Select_Temp(TemplateView):pass
class Add_4_Temp_content(TemplateView):pass