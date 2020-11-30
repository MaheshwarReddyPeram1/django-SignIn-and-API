
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from check.models import Courses

@api_view(['GET'])
def getCourse(request):
    course=Courses()
    course.courseName = "Html and Css"
    course.titleName= "Html and css are used to build front end web pages which gives content structure and meaning  to the web page"
    course.tags= "Html, css, javascript"
    course.color1= "#fdecf3"
    course.color2= "#ec509b"
    course.from_age= 9
    course.to_age= 11

    
    course1=Courses()
    course1.courseName = "Html and Css"
    course1.titleName= "Html and css are used to build front end web pages which gives content structure and meaning  to the web page"
    course1.tags= "Html, css, javascript"
    course1.color1= "#fdecf3"
    course1.color2= "#ec509b"
    course1.from_age= 9
    course1.to_age= 11

    course2=Courses()
    course2.courseName = "Html and Css"
    course2.titleName= "Html and css are used to build front end web pages which gives content structure and meaning  to the web page"
    course2.tags= "Html, css, javascript"
    course2.color1= "#fdecf3"
    course2.color2= "#ec509b"
    course2.from_age= 9
    course2.to_age= 11

    course3=Courses()
    course3.id = 3
    course3.courseName = "Java"
    course3.titleName= "Ruby is an interpreted and high level programming language, mainly used for Server side web development framework"
    course3.tags= "Html, css, javascript"
    course3.color1= "#f8efff"
    course3.color2= "#bd5ffd"
    course3.from_age= 9
    course3.to_age= 11

    finacourse=[
        course,
        course1,
        course2,
        course3
    ]

    
    serializer = TaskSerializer(finacourse, many=True)
    # serializer1 = TaskSerializer(course, many=False)
    return Response({
        # "serializer1":serializer1.data,
        "serializer":serializer.data
        })