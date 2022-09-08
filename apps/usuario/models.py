from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password= None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        usuario = self.model(
            username= username,
            email= self.normalize_email(email),
            nombres= nombres,
            apellidos= apellidos
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username,email, nombres, apellidos, password):
        usuario = self.create_user(
            email,
            username= username,
            nombres= nombres,
            apellidos= apellidos,
            password= password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique= True, max_length= 50)
    email = models.EmailField('Correo electronico', unique= True , max_length= 254)
    nombres = models.CharField('Nombres', max_length= 200, blank= True, null= True)
    apellidos = models.CharField('Apellidos', max_length= 200, blank= True, null= True)
    usuario_activo = models.BooleanField(default= True)
    usuario_administrador = models.BooleanField(default= False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    """ Permisos para ingresar al administrador """
    def has_perm(self,perm,ob = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
