# Generated by Django 5.0.2 on 2024-02-29 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Omershark', max_length=50, null=True, verbose_name='name')),
                ('address', models.CharField(blank=True, default='25 jalal Eldin.st El-Nozha', max_length=50, null=True, verbose_name='address')),
                ('salary', models.IntegerField(default=5000, verbose_name='salary')),
                ('added_in', models.DateField(auto_now_add=True)),
                ('job', models.CharField(choices=[('Grphic designer', 'Grphic designer'), ('web_dev(front-end)&wordpress', 'web_dev(front-end)&wordpress'), ('web_dev(back-end)', 'web_dev(back-end)'), ('web_dev(full-stack)', 'web_dev(full-stack)'), ('Selles & Marketing', 'Selles & Marketing'), ('Outher', 'Outher')], default=('web_dev(back-end)', 'web_dev(back-end)'), max_length=50, verbose_name='job title')),
                ('cv_file', models.FileField(default='cv.docx', upload_to='emp_cv_doc', verbose_name='cv file')),
                ('mail', models.EmailField(blank=True, default='someone1111@gmail.com', max_length=250, null=True, verbose_name='your Email')),
                ('phone', models.BigIntegerField(default=1094128969, verbose_name='your phonenumber')),
            ],
            options={
                'verbose_name': 'Employee_model',
                'verbose_name_plural': 'Employee_model',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Four_pages_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Four_pages_model',
                'verbose_name_plural': 'Four_pages_models',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='weboku website', max_length=100, null=True, verbose_name='project name')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('proj_link', models.URLField(default='https://pypi.org/project/django-countries/', max_length=300, verbose_name='project/post url')),
                ('proj_img', models.ImageField(default='proj_img.jpg', upload_to='project adv model')),
                ('bio', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis quaerat beatae iste dolorum quas dolore qui cum blanditiis magni distinctio aut dolores quasi officia quam, nihil perferendis, earum amet quibusdam?', max_length=300, verbose_name='project details')),
                ('proj_type', models.CharField(choices=[('Paid SOCIAL MEDIA MARKETING ', 'Paid SOCIAL MEDIA MARKETING '), ('Content marketing', 'Content marketing'), ('Web development And Web design', 'Web development And Web design'), ('Full service marketing agencies', 'Full service marketing agencies'), ('E-COMMERCE SOLUTIONS', 'E-COMMERCE SOLUTIONS'), ('Advertising', 'Advertising'), ('Email marketing,', 'Email marketing,'), ('SEO branding', 'SEO branding'), ('Outher', 'Outher')], default=('Web development And Web design', 'Web development And Web design'), max_length=50, verbose_name='service type')),
                ('added_in', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Projects',
                'verbose_name_plural': 'Projects',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Service_offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_offer', models.CharField(blank=True, choices=[('Paid SOCIAL MEDIA MARKETING ', 'Paid SOCIAL MEDIA MARKETING '), ('Content marketing', 'Content marketing'), ('Web development And Web design', 'Web development And Web design'), ('Full service marketing agencies', 'Full service marketing agencies'), ('E-COMMERCE SOLUTIONS', 'E-COMMERCE SOLUTIONS'), ('Advertising', 'Advertising'), ('Email marketing,', 'Email marketing,'), ('SEO branding', 'SEO branding'), ('Outher', 'Outher')], default=('Web development And Web design', 'Web development And Web design'), max_length=50, null=True, verbose_name='servic offer for')),
                ('offer_img', models.ImageField(default='offer.jpg', upload_to='offer_adv')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='title')),
                ('bio', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis quaerat beatae iste dolorum quas dolore qui cum blanditiis magni distinctio aut dolores quasi officia quam, nihil perferendis, earum amet quibusdam?', max_length=300, verbose_name='client request')),
                ('offer_cost', models.IntegerField(blank=True, default=150, null=True, verbose_name='ofer_cost')),
            ],
            options={
                'verbose_name': 'Service_offers',
                'verbose_name_plural': 'Service_offers',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client_country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='egypt', max_length=50, verbose_name='country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_country', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client_country',
                'verbose_name_plural': 'Client_country',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asker', models.CharField(blank=True, max_length=90, null=True, verbose_name='askier')),
                ('img_bkg', models.ImageField(default='user_bkg_1.jpg', upload_to='Client_bkg_img')),
                ('img_logo', models.ImageField(default='user_logo.jpg', upload_to='Client_logo_img')),
                ('phone', models.BigIntegerField(default=1094128969, verbose_name='your phonenumber')),
                ('bio', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis quaerat beatae iste dolorum quas dolore qui cum blanditiis magni distinctio aut dolores quasi officia quam, nihil perferendis, earum amet quibusdam?', max_length=300, verbose_name='client request')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='question_from', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client_requests',
                'verbose_name_plural': 'Client_requests',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Service_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='website/ web app', max_length=50, null=True, verbose_name='Add content')),
                ('serv_logo', models.ImageField(default='serv.jpg', upload_to='service_logos')),
                ('bio', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis quaerat beatae iste dolorum quas dolore qui cum blanditiis magni distinctio aut dolores quasi officia quam, nihil perferendis, earum amet quibusdam?', max_length=300, verbose_name='service')),
                ('serv_cost', models.IntegerField(default=1500, verbose_name='cost')),
                ('provided_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_by', to='core.employee_model')),
            ],
            options={
                'verbose_name': 'Service_name',
                'verbose_name_plural': 'Service_name',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Template_web_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='ِA 4 pages Webstie model', max_length=40, null=True)),
                ('temp_link', models.URLField(default='', max_length=300, verbose_name='template_link')),
                ('for_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='static_website_for', to='core.service_offers')),
            ],
            options={
                'verbose_name': 'Template_web_model',
                'verbose_name_plural': 'Template_web_model',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
