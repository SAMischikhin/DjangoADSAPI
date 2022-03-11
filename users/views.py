from ads.models import User

from users.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView,\
    DestroyAPIView, RetrieveAPIView


class UserListView(ListAPIView):
    queryset = User.objects.all()#order_by("username")
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
