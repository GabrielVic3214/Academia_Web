from django import forms

from .models import Usuario, Parceiro, Modalidade

class UserForm(forms.ModelForm):

    nome = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'inputdetails',
                'placeholder': 'Nome'
            }
        )
    )

    sobrenome = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'inputdetails',
                'placeholder': 'Sobrenome'
            }
        )
    )
    idade = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'inputdetails ',
                'placeholder': 'Idade'
            }
        )
    )
    Email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'inputdetails',
                'placeholder': 'Email'
            }
        )
    )

    tel1 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'inputdetails'}
        )
    )

    tel2 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'inputdetails'}
        )
    )

    cpf = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'inputdetails'}
        )
    )

    cep = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'inputdetails'}
        )
    )

    Bairro = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'inputdetails'}
        )
    )

    Estado = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'inputdetails'}
        )
    )

    Cidade = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'inputdetails'}
        )
    )

    Rua = forms.CharField(
            max_length=255,
            widget=forms.TextInput(
                attrs={'class': 'inputdetails'}
            )
        )
    
    senha = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'digite sua senha', 'class': 'inputdetails'}
        )
    )

    class Meta:
        model = Usuario
        fields = ('nome', 'sobrenome', 'idade', 'Email', 'tel1', 'tel2',
                  'cpf', 'cep', 'Bairro', 'Estado', 'Cidade', 'Rua', 'senha')
        

class Form_Parceiro(forms.ModelForm):

    NomEmp = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome da Empresa'}
        )
    )

    NomFantasia = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome Fantasia'}
        )
    )

    cnpj = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'cnpj'}
        )
    )

    telefone = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': '(00)00000-0000'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email'}
        )
    )

    cep = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Cep'}
        )
    )

    estado = forms.CharField(
        max_length=255,
        widget=forms.TextInput()
    )

    rua = forms.CharField(
        max_length=255,
        widget=forms.TextInput()
    )

    bairro = forms.CharField(
        max_length=255,
        widget=forms.TextInput()
    )

    senha = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'digite sua senha'}
        )
    )

    class Meta:
        model = Parceiro
        fields = ('NomEmp', 'NomFantasia', 'cnpj','telefone', 'email',
                  'cep', 'estado', 'rua', 'bairro', 'senha')
        
class FormModalidade(forms.ModelForm):

    NomMod = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome da modalidade'}
        )
    )

    QuantAlu = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Quantidade de alunos'}
        )
    )

    DescMod = forms.CharField(
        max_length=400,
        widget=forms.Textarea(
            attrs={'placeholder': 'Breve descrição modalidade'}
        )
    )

    class Meta:
        model = Modalidade
        fields = '__all__'