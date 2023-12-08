from rest_framework import serializers
from users.models import User, Student, Teacher, Admin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",  "email", "is_teacher",
                  "is_student", "is_admin"]


class StudentSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        model = Admin
        fields = "__all__"


class Student_RegisterSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(style={"input_type": "password"},
                                                  max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email",
                  "phone", "password", "password_confirmation",
                  ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"]
        )

        password = self.validated_data["password"]
        password_confirmation = self.validated_data["password_confirmation"]
        if password_confirmation != password:
            raise ValueError({"error": "Passwords do not match"})
        user.set_password(password)
        user.is_student = True
        user.first_name = self.validated_data["first_name"]
        user.last_name = self.validated_data["last_name"]
        user.phone = self.validated_data["phone"]
        try:
            user.save()
            Student.objects.create(user=user)

        except Exception as exception_message:
            return exception_message

        return user


class Teacher_RegisterSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(style={"input_type": "password"},
                                                  max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email",
                  "phone", "password", "password_confirmation",
                  ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"]
        )

        password = self.validated_data["password"]
        password_confirmation = self.validated_data["password_confirmation"]
        if password_confirmation != password:
            raise ValueError({"error": "Passwords do not match"})
        user.set_password(password)
        user.is_teacher = True
        user.first_name = self.validated_data["first_name"]
        user.last_name = self.validated_data["last_name"]
        user.phone = self.validated_data["phone"]
        try:
            user.save()
            Teacher.objects.create(user=user)

        except Exception as exception_message:
            return exception_message

        return user


class Admin_RegisterSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(style={"input_type": "password"},
                                                  max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email",
                  "phone", "password", "password_confirmation",
                  ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"]
        )

        password = self.validated_data["password"]
        password_confirmation = self.validated_data["password_confirmation"]
        if password_confirmation != password:
            raise ValueError({"error": "Passwords do not match"})
        user.set_password(password)
        user.is_admin = True
        user.first_name = self.validated_data["first_name"]
        user.last_name = self.validated_data["last_name"]
        user.phone = self.validated_data["phone"]
        try:
            user.save()
            Admin.objects.create(user=user)

        except Exception as exception_message:
            return exception_message

        return user


class Profile_Update_Serializer(serializers.ModelSerializer):

    company_name = serializers.CharField(max_length=50, required=False)
    wilaya = serializers.CharField(max_length=2, required=False)
    phone = serializers.CharField(max_length=13, required=False)
    CNN = serializers.CharField(max_length=18, required=False)
    birthdate = serializers.DateField()
    extrait_de_naissance = serializers.CharField(max_length=25, required=False)
    registre_commerce = serializers.CharField(max_length=25, required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email",
                  "company_name",  "wilaya", "phone", "CNN",
                  "birthdate",
                  "extrait_de_naissance", "registre_commerce"]

    def save(self, user,  *args, **kwargs):

        user_var = User.objects.get(username=user.username)
        Simple_user = Student.objects.get(user=user)

        user_fields = ["first_name", "last_name", "email"]
        simple_user_fields = ["company_name",  "wilaya", "phone", "CNN",
                              "birthdate",
                              "extrait_de_naissance", "registre_commerce"]

        # setting the new infos in User Table
        for field in user_fields:
            if field in self.validated_data:
                setattr(user_var, field, self.validated_data[field])

        # setting the infos of SimpleUser Table
        for field in simple_user_fields:
            if field in self.validated_data:
                setattr(Simple_user, field, self.validated_data[field])

        try:
            user_var.save()
        except:
            return "Un utilisateur avec cet email existe déja"

        try:
            Simple_user.save()
        except:
            return "Un utilisateur avec ce CNN existe déja"

        return Simple_user
