from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework import generics, response, status, permissions
from .serializers import UserSerializer, Student_RegisterSerializer, Teacher_RegisterSerializer, Admin_RegisterSerializer

# Create your views here.


class Student_RegisterView(generics.GenericAPIView):
    serializer_class = Student_RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            success_message = {"answer": "success",
                               "token": Token.objects.get(user=user).key,
                               "message": "Student is created successfully",
                               }
            return response.Response(success_message, status=status.HTTP_201_CREATED)

        error_message = {"answer": "error",
                         "errors": serializer.errors
                         }
        return response.Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class Teacher_RegisterView(generics.GenericAPIView):
    serializer_class = Teacher_RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            success_message = {"answer": "success",
                               "token": Token.objects.get(user=user).key,
                               "message": "Teacher is created successfully",
                               }
            return response.Response(success_message, status=status.HTTP_201_CREATED)

        error_message = {"answer": "error",
                         "errors": serializer.errors
                         }
        return response.Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class Admin_RegisterView(generics.GenericAPIView):
    serializer_class = Admin_RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            success_message = {"answer": "success",
                               "token": Token.objects.get(user=user).key,
                               "message": "Admin is created successfully",
                               }
            return response.Response(success_message, status=status.HTTP_201_CREATED)

        error_message = {"answer": "error",
                         "errors": serializer.errors
                         }
        return response.Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class Custom_Auth_Token(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            success_message = {
                "answer": "success",
                "token": token.key,
            }

            return response.Response(success_message, status=status.HTTP_200_OK)

        error_message = {"answer": "error",
                         "errors": serializer.errors
                         }
        return response.Response(error_message, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request, format=None):
        if request.auth:
            request.auth.delete()
            success_message = {
                "answer": "success",
            }
            return response.Response(success_message, status=status.HTTP_200_OK)

        error_message = {"answer": "error",
                         }
        return response.Response(error_message, status=status.HTTP_400_BAD_REQUEST)
