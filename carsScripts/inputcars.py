import sys
import os
import pandas as pd
from django.utils import timezone

sys.path.append("/home/russ/Desktop/Python/Cars/mysite")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
import django
django.setup()

from cars.models import CarsInfo
# Make Model Release Year Image Link
data = sys.argv[1]  
df = pd.read_csv(data)


for i in range(0,len(df.index)):
	q = CarsInfo(make = df.iloc[i]['Make'],model = df.iloc[i]['Model'],
		release_year=df.iloc[i]['Release Year'], car_pic=df.iloc[i]['Image Link'],
		pub_date=timezone.now())
	q.save()

for row in CarsInfo.objects.all():
    if CarsInfo.objects.filter(model=row.model).count() > 1:
        row.delete()