from django.urls import *
from django.contrib.auth import views as auth_x
from .views import *



urlpatterns = [
     path('',Home_page.as_view(),name='home'),
     path('add_user',Register_form.as_view(),name='add_user'),
     #for the client
     path('add_user/from_country',Register_form.as_view(),name='your_country'),
     path('client_profile_of_x',Register_form.as_view(),name='user_country'),
     #for the Employee
     path('emp_type',employee_type_list,name='emp_type'),
     path('emp_type/Emp_list_of<str:e_type>',emp_list,name='emp_list'),
     path('emp_type/Emp_list_of<str:e_type>/emp_id<int:e_id>',emp_item,name='emp_item'),
     #for the Projects
     
     path('proj_list',Proj_sectors.as_view(),name='proj_type'),
     path('proj_list/filter_<str:type_x>',proj_data,name='proj_list'),
     path('proj_list/filter_<str:type_x>/proj_of_id<int:p>',proj_item,name='proj_item'),
     #auth actions
     #-------------------------------------------------------------------------------
     path('login',auth_x.LoginView.as_view(template_name='registration/login.html'),name="login"),
     path('logout',auth_x.LogoutView.as_view(),name="logout"),
     #-------------------------------------------------------------------------------
     #service_begin(select service)
     path('select_service',Select_service.as_view(),name='find_service'),
     #in case of normal services
     path('select_service/offers_of_<str:o>',Select_service_offers.as_view(),name='serv_offers'),
     path('select_service/offers_of_<str:o>/offer_Num<int:id>',offer_item,name='offer_item'),
     #in case of website and after selecting 'website service' show the 3 offers but foucs on the 1st offer (static website)
     path('select_service/offers/select_web_temp',Select_Temp.as_view(),name='find_temp'),
     path('select_service/offers/select_web_temp/add_contents',Add_4_Temp_content.as_view(),name='find_temp'),    
]