from rest_framework import serializers
from check.models import Courses

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Courses
		fields ='__all__'