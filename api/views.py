from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import TaskSerializer
from base.models import Task

@api_view(['GET'])
def getRoutes(request):

    routes=[
        {'GET':'api/tasks'},
        {'GET':'api/tasks/<int:pk>'},
        {'POST':'api/task-add'},
        {'PUT':'api/task-update/<int:pk>'},
        {'DELETE':'api/task-delete/<int:pk>'},

        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getTasks(request):
    # print('USER:',request.user)
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getTask(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer=TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response('Item Succesesfully deleted!!!')
    # serializer=TaskSerializer(task,many=False)
    # return Response(serializer.data)
