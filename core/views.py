from django.shortcuts import render
from .forms import DatabaseForm
  
from django.http import JsonResponse
from core.models import databases


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import DataSeriallizer

import os
import zipfile


def index(request):
    form = DatabaseForm()

    if request.method == 'POST':
        print(request.POST)
        form= DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            
    context ={'form':form}
    return render(request,'home.html',context)



class TestView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request, *args, **kwargs):
        qs= databases.objects.all()
        serializer = DataSeriallizer(qs, many=True)
        return  Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = DataSeriallizer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    





def  database_detail_view(request):
    all_database = databases.objects.all()
    for content in all_database: 
        print(content)
        DB_HOST = 	content.IP 
        DB_USER = content.UserName
        DB_USER_PASSWORD = content.Password

        DB_NAME = content.DBname
        BACKUP_PATH = 'F:\\backitup'
        ZIP_BACKUP= 'F:\\backitup\zip_backup'


        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + BACKUP_PATH + "/" + DB_NAME + ".sql"
        os.system(dumpcmd)

        handle = zipfile.ZipFile('Sql-DB.zip','w')
        os.chdir('F:\\backitup')
        
        for x in os.listdir():
            if x.endswith('.sql'):
                handle.write(x, compress_type= zipfile.ZIP_DEFLATED)
        handle.close()
    
        
       
    return render (request,'detail.html',{'data':all_database})


def ListOfDatabase(request):
    listdatabase = databases.objects.all()
    return render(request,'display.html',{'list':listdatabase})

