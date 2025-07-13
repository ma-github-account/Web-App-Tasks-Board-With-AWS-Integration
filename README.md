This Django application is Tasks Board. Application is integrated with AWS. Storage is in S3 service. Database
is in RDS service. The application is deployed in AWS infrastructure using Elastic Beanstalk.

The application is available here: https://www.michaldomain.com/

The folder contains two versions of application: basic one run locally and aws integrated.

1.Basic version

Prerequisites:

- Python 3.9.7,
- Django 4.1.2,

How to run: 1.python manage.py makemigrations 2.python manage.py migrate 3.python manage.py runserver

2.Version with AWS integration.

Prerequisites:
- AWS account
- AWS S3 bucket with policy allowing public access
- After creating S3 bucket static files need to be migrated using command: python manage.py collectstatic
- Django Storages (pip install django-storages)
- Boto3 (pip install boto3)
- Psycopg2-binary (pip install psycopg2-binary)
- PostgresSQL database in AWS RDS Service with public access
- Pyyaml and Awsebcli (pip install pyyaml==5.3.1 awsebcli)
- Gunicorn (pip install gunicorn)
- After deploying to Elastic Beanstalk environment variables used in file settings.py need to be added to Elastic Beanstalk. Variables: SECRET_KEY, NAME, USER, PASSWORD, HOST, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
- In settings.py file parameters ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS need to be updated to match your host environment

Elastic Beanstalk commands to deploy the application:
1.eb init
2.eb create
3.eb deploy (in case the changes were made and the application needs to be updated in EB)

![1](https://github.com/user-attachments/assets/cf4392f6-605e-43d9-8626-908e1cc435fb)



![2](https://github.com/user-attachments/assets/310cf614-b14c-4176-a867-738f55977544)

















