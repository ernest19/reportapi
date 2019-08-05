from galamsey.models import *
from charcoal.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields=("last_login","username","last_name","email","password")


class ReportSerializers(serializers.ModelSerializer):
	class Meta:
		model = incidentReports
		fields=("Description","status","image","voice","lat","lng")



class charcoalSerializers(serializers.ModelSerializer):
	class Meta:
		model = charcoalReports
		fields=("Description","status","image","voice","lat","lng")

		
# 
# class BinSerializers(serializers.ModelSerializer):
# 	class Meta:
# 		model = Bin
# 		fields=("bin_code","bin_name","allocation_status","date_created","bin_colour","bin_size","bin_type","bin_unit_price","bin_quantity")

# 		