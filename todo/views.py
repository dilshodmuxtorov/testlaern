from rest_framework import generics
from .models import TodoModel
from .serializers import TodoModelSerializer
from rest_framework.response import Response

class TodoListView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer

class TodoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer

class DoneView(generics.GenericAPIView):
    serializer_class = TodoModelSerializer

    def post(self, request):
        todo_id = request.data.get('todo_id')

        try:
            todo = TodoModel.objects.get(id = todo_id)
            todo.is_done = True
            todo.save()
            return Response("Bajarildi")
        except TodoModel.DoesNotExist:
            return Response("Todo model topilmadi")