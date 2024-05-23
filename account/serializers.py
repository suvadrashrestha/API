from rest_framework import serializers
from .models import User
from .utils import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this because we need to confirm password filed in our registration request
    #this doesnot include the password2 in response object
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields=['email','name','password','password2','tc']
        extra_kwargs={
            'password':{'write_only':True}
        }

    #validating password and confirm password while registration


  # this function runs when is_valid method is called on instance of UserRegistrationSerializer
    def validate(self, attrs):
        # print(attrs)
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError("password and confirm password doenot match")
        return attrs
    
    def create(self,data):
        #the data contains the validate_data data
       # print(data)
        return User.objects.create_user(**data)


class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','name']

class UserChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)
    password2=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)
    class Meta:
        fields=["password","password2"]
    def validate(self, attrs):
        password=attrs.get("password")
        password2=attrs.get("password2")
        #is the way to extract data passed in context
        user=self.context.get("user")
        if(password!=password2):
            raise serializers.ValidationError("password and confirm password doenot match")
        user.set_password(password)
        user.save()
        return attrs
       

class SendpasswordResetEmailSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        fields=["email"]
    def validate(self, attrs):
        email=attrs.get("email")
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            # urlsafe_base64_encode takes byte and forrce_bytes changes data into byte 
            uid=urlsafe_base64_encode(force_bytes(user.id))
            print("Encoded UID", uid)
            token=PasswordResetTokenGenerator().make_token(user)
            print('password Resst Token',token)
            link='http://localhost:3000/api/user/reset/'+uid+'/'+token
            print("password reset link " ,link)
            body="click Following Link to reset your Password"+"  "+link
            data={
                "subject":"Reset your password",
                "body":body,
                "to_email":user.email        
            }
            Util.send_email(data)
            return attrs

        else:
            raise serializers.ValidationError("You are not a registered User")

class UserPasswordResetSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)
    password2=serializers.CharField(max_length=255,style={"input_type":"password"},write_only=True)
    class Meta:
        fields=["password","password2"]
    def validate(self, attrs):
        try:
            password=attrs.get("password")
            password2=attrs.get("password2")
            #is the way to extract data passed in context
            uid=self.context.get("uid")
            token=self.context.get("token")

            if(password!=password2):
                raise serializers.ValidationError("password and confirm password doenot match")
            id=smart_str(urlsafe_base64_decode(uid))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError("Token is not valid or expired")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError("Token is not valid or expired")
