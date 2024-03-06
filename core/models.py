from django.db import models
from django.contrib.auth.models import User
#from .Gene_serve import *
#from .Gene_client import *
#from django_countries.fields import Countries




detil='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis quaerat beatae iste dolorum quas dolore qui cum blanditiis magni distinctio aut dolores quasi officia quam, nihil perferendis, earum amet quibusdam?'
Serv=(('Paid SOCIAL MEDIA MARKETING ','Paid SOCIAL MEDIA MARKETING '),
      ('Content marketing','Content marketing'),
      ('Web development And Web design','Web development And Web design'),
      ('Full service marketing agencies','Full service marketing agencies'),
      ('E-COMMERCE SOLUTIONS','E-COMMERCE SOLUTIONS'),
      ('Advertising','Advertising'),
      ('Email marketing,','Email marketing,'),
      ('SEO branding','SEO branding'),
      ('And more','And more'))
Job=(('Grphic designer','Grphic designer'),
     ('web_dev(front-end)&wordpress','web_dev(front-end)&wordpress'),
     ('web_dev(back-end)','web_dev(back-end)'),
     ('web_dev(full-stack)',
      'web_dev(full-stack)'),
     ('Selles & Marketing','Selles & Marketing'),
     ('Outher','Outher'))     
# Create your models here.
class Client_country(models.Model):
      user = models.ForeignKey(User,related_name='from_country', on_delete=models.CASCADE)
      country=models.CharField(verbose_name="country",default="egypt", max_length=50)
      

      def __str__(self):return str(self.pk)+":"+self.user

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Client_country'
            verbose_name_plural = 'Client_country'






class Employee_model(models.Model):
      name = models.CharField(max_length=50, blank=True, null=True,verbose_name="name",default="Omershark")
      address = models.CharField(max_length=50, blank=True, null=True,verbose_name="address",default="25 jalal Eldin.st El-Nozha")
      salary = models.IntegerField(default=5000,verbose_name="salary")
      added_in = models.DateField(auto_now_add=True)
      img_bkg = models.ImageField(upload_to='emp_img', height_field=None, width_field=None, max_length=100,default='user_bkg_1.jpg')
      
      job = models.CharField(max_length=50,verbose_name="job title",choices=Job,default=Job[2])
      cv_file = models.FileField(upload_to='emp_cv_doc',verbose_name='cv file', max_length = 100,default='cv.docx')
      mail = models.EmailField(max_length=250,verbose_name="your Email",default="someone1111@gmail.com", blank=True, null=True)
      phone = models.BigIntegerField(verbose_name="your phonenumber",default=1094128969)
      
      
      
      

      def __str__(self):
            return str(self.pk)+":"+self.name

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Employee_model'
            verbose_name_plural = 'Employee_model'




#-----------------------------NO NEED TO DISPLAY SERVICE MODEL.....USER THE 'serv' list for all actions----------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

class Service_name(models.Model):
      name = models.CharField(max_length=50,verbose_name="Add content", blank=True, null=True,default="website/ web app")
      provided_by= models.ForeignKey(Employee_model, related_name='provided_by', on_delete=models.CASCADE)
      serv_logo = models.ImageField(upload_to='service_logos', height_field=None, width_field=None, max_length=100,default='serv.jpg')
      bio = models.TextField(default=detil,max_length=300,verbose_name = 'service')
      serv_cost= models.IntegerField(default=1500,verbose_name="cost")
      
      

      def __str__(self):
            return str(self.pk)+":"+self.name

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Service_name'
            verbose_name_plural = 'Service_name'

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

class Service_offers(models.Model):
      #offer_for = models.ForeignKey(Service_name, related_name='has_offer_of', on_delete=models.CASCADE)
      serv_offer = models.CharField(max_length=50, blank=True, null=True,verbose_name="servic offer for",choices=Serv,default=Serv[2])
      '''
      لأضافة بوست سوشيال ميديا
      '''
      offer_img = models.ImageField(upload_to='offer_adv', height_field=None, width_field=None, max_length=100,default="offer.jpg")
      title = models.CharField(max_length=30,blank=True, null=True,verbose_name="title")
      bio = models.TextField(default=detil,max_length=300,verbose_name = 'client request')
      offer_cost= models.IntegerField(default=150,blank=True, null=True,verbose_name="ofer_cost")
      

      def __str__(self):
            return str(self.pk)+":"+self.serv_offer

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Service_offers'
            verbose_name_plural = 'Service_offers'


class Projects(models.Model):
      title = models.CharField(max_length=100, blank=True, null=True,default="weboku website",verbose_name="project name")
      name = models.CharField(max_length=30,blank=True, null=True)
      proj_link = models.URLField(max_length = 300,default="https://pypi.org/project/django-countries/",verbose_name="project/post url")
      proj_img = models.ImageField(upload_to='project adv model', height_field=None, width_field=None, max_length=100,default='proj_img.jpg')
      bio = models.TextField(default=detil,max_length=300,verbose_name = 'project details')
      proj_type = models.CharField(max_length=50,verbose_name="service type",choices=Serv,default=Serv[2])
      added_in = models.DateTimeField( auto_now_add=True)
      
      
      
      

      def __str__(self):return str(self.pk)+":"+self.title

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Projects'
            verbose_name_plural = 'Projects'


#-----------------------------NEED A BIG REVIEW----------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
class Template_web_model(models.Model):
      '''
       
         من أحل الويب...حيث انه من الممكن ان  تكون خدمه الويب تتيخ عرض البرونزية لصغخات الويب والذي يشمل 4صفحات من قالب متوفر رايطه هنا في هذا المكان
      '''
      name = models.CharField(max_length=40, blank=True, null=True,default="ِA 4 pages Webstie model")
      for_offer = models.ForeignKey(Service_offers,related_name="static_website_for", on_delete=models.CASCADE)
      temp_link = models.URLField(default="",verbose_name="template_link",max_length = 300)
      

      

      def __str__(self):
            return str(self.pk)+":"+self.name

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Template_web_model'
            verbose_name_plural = 'Template_web_model'


'''
  Four_pages_modelبعد أختيار النموذح يتم التحويل الي أستماره 


 '''
class Four_pages_model(models.Model):

      def __str__(self):
            pass

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Four_pages_model'
            verbose_name_plural = 'Four_pages_models'


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------            



class Co_operators(models.Model):
      name = models.CharField(max_length=90,blank=True, null=True,verbose_name="askier",default="Markus")
      img_logo = models.ImageField(upload_to='co_img', height_field=None, width_field=None, max_length=100,default='user_logo.jpg')
      phone = models.BigIntegerField(verbose_name="your phonenumber",default=1094128969)
      bio = models.TextField(default=detil,max_length=300,verbose_name = 'client request')
      def __str__(self):
            return "co operator"+str(self.pk)+":"+self.name

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Co_operators'
            verbose_name_plural = 'Co_operators'
      


class Client_requests(models.Model):
      user = models.OneToOneField(User,related_name='question_from', on_delete=models.CASCADE)
      asker = models.CharField(max_length=90,blank=True, null=True,verbose_name="askier")
      img_bkg = models.ImageField(upload_to='Client_bkg_img', height_field=None, width_field=None, max_length=100,default='user_bkg_1.jpg')
      img_logo = models.ImageField(upload_to='Client_logo_img', height_field=None, width_field=None, max_length=100,default='user_logo.jpg')
      phone = models.BigIntegerField(verbose_name="your phonenumber",default=1094128969)
      
      bio = models.TextField(default=detil,max_length=300,verbose_name = 'client request')
      
      
      
      

      def __str__(self):
            return "question num"+str(self.pk)+":"+self.asker

      class Meta:
            db_table = ''
            ordering = ('pk',)
            managed = True
            verbose_name = 'Client_requests'
            verbose_name_plural = 'Client_requests'


all_clients=Client_country.objects.all()
filt_clients=Client_country.objects.filter(country=True)

#-------------------all sorts employees--------------------
all_emps=Employee_model.objects.all()
emp_dg=Employee_model.objects.filter(job=Job[0])
emp_web_front=Employee_model.objects.filter(job=Job[1])
emp_web_back=Employee_model.objects.filter(job=Job[2])
emp_web_full=Employee_model.objects.filter(job=Job[3])
emp_sell=Employee_model.objects.filter(job=Job[4])
emp_unkown_job=Employee_model.objects.filter(job=Job[5])
#---------------------------------------------------------




#-------------------all sorts projects--------------------
all_proj=Projects.objects.all()
proj_social_camp=Projects.objects.filter(proj_type=Serv[0])
proj_content_making=Projects.objects.filter(proj_type=Serv[1])
proj_web_dev=Projects.objects.filter(proj_type=Serv[2])
proj_serve_market=Projects.objects.filter(proj_type=Serv[3])
proj_e_commerce_sol=Projects.objects.filter(proj_type=Serv[4])
proj_adv_act=Projects.objects.filter(proj_type=Serv[5])
proj_mail_market=Projects.objects.filter(proj_type=Serv[6])
proj_seo_service=Projects.objects.filter(proj_type=Serv[7])
proj_unkown=Projects.objects.filter(proj_type=Serv[8])
#---------------------------------------------------------



#-------------------all sorts Service offers--------------------
all_offers=Service_offers.objects.all()
offer_social_camp=Service_offers.objects.filter(serv_offer=Serv[0])
offer_content_making=Service_offers.objects.filter(serv_offer=Serv[1])
offer_web_dev=Service_offers.objects.filter(serv_offer=Serv[2])
offer_serve_market=Service_offers.objects.filter(serv_offer=Serv[3])
offer_e_commerce_sol=Service_offers.objects.filter(serv_offer=Serv[4])
offer_adv_act=Service_offers.objects.filter(serv_offer=Serv[5])
offer_mail_market=Service_offers.objects.filter(serv_offer=Serv[6])
offer_seo_service=Service_offers.objects.filter(serv_offer=Serv[7])
offer_unkown=Service_offers.objects.filter(serv_offer=Serv[8])
#---------------------------------------------------------
