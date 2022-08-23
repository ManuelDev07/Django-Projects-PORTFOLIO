from django import forms

#Formulario para la app Contact:
class ContactForm(forms.Form):
    #Cada variable será el campo para escribir:
    name = forms.CharField(label='Nombre', required=True)
    email = forms.CharField(label='Correo Electrónico', required=True)
    subject = forms.CharField(label='Asunto', widget=forms.Textarea) #Para que en vez de ser un input común sea una textarea tag