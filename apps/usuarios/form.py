# Criar objetos

from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Exemplo: João da Silva"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
            
    )
    
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome completo",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Exemplo: João da Silva"
            }
        )
    )
    email=forms.EmailField(
        label="Email de cadastro",
         required=True,
         max_length=100,
         widget=forms.EmailInput(
             attrs={
                 "class": "form-control",
                 "placeholder": "Exemplo: joaosilva@teste.com"
             }
         )
         
    )
    senha1 =forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
            
    )
    senha2 =forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua novamente"
            }
        )
            
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip() # Retirar os espaços do inicio e do final
            if " " in nome:
                raise forms.ValidationError("Espaço não são permitidos nesse campo")
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2