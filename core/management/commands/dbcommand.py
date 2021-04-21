from django.core.management.base import BaseCommand
from core.views import database_detail_view
from core.models import databases
import os
import zipfile
class Command (BaseCommand):

    def handle(self, *args, **kwargs):
        all_database = databases.objects.all()
        for content in all_database: 
            print(content)
            DB_HOST = 	content.IP 
            DB_USER = content.UserName
            DB_USER_PASSWORD = content.Password

            DB_NAME = content.DBname
            BACKUP_PATH = 'F:\\backitup'
            


            dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + BACKUP_PATH + "/" + DB_NAME + ".sql"
            os.system(dumpcmd)


            handle = zipfile.ZipFile('Sql-DB.zip','w')
            os.chdir('F:\\backitup')
        
            for x in os.listdir():
                    if x.endswith('.sql'):
                        handle.write(x, compress_type= zipfile.ZIP_DEFLATED)
            handle.close()
    
