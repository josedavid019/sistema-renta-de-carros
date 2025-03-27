from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

Usuario = get_user_model()


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'telefono']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(**validated_data)
        return usuario


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        usuario = authenticate(username=data['username'], password=data['password'])
        if not usuario:
            raise serializers.ValidationError("Credenciales incorrectas")

        refresh = RefreshToken.for_user(usuario)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
