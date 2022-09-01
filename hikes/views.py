from rest_framework import generics
from .models import Hike
from .serializers import HikeSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class HikeList(generics.ListCreateAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer


class HikeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
