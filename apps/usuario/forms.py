from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
    """Formulario de registro de un usuario en la base de datos

    Variables:

        -password1: contraseña
        -password2: verificacion de contraseña

    """
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput(
        attrs = {
        'class': 'form-control',
        'placeholder': 'Ingrese su contraseña',
        'id': 'password1',
        'required': 'required',
        }
    ))

    password2 = forms.CharField(label= 'Contraseña de verificación', widget= forms.PasswordInput(
    attrs = {
    'class': 'form-control',
    'placeholder': 'Verifique su contraseña',
    'id': 'password2',
    'required': 'required',
    }
    ))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos', 'usuario_activo', 'usuario_administrador')
        labels = {
        'usuario_activo': 'Usuario',
        'usuario_administrador': 'Administrador'
        }
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
                'autocomplete': 'off'
                }
            ),
            'nombres': forms.TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre',
                'pattern': '[A-Z a-z]*',
                'title': 'No se permiten números',
                'autocomplete': 'off'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'ingrese su apellido',
                'pattern': '[A-Z a-z]*',
                'title': 'No se permiten números',
                'autocomplete': 'off'
                }
            ),
            'username': forms.TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de usuario',
                'autocomplete': 'off'
                }
            ),
        }

    def clean_password2(self):
        """Validacion de contraseña

        Metodo que valida que ambas contraseñas sean iguales, antes de ser encriptadas
        y almacenadas en la base de datos, Retornar la contraseña valida.

        Excepcion:
        -   ValidationError --cuando las contraseñas no son iguales se muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
