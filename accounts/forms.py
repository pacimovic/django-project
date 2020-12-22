from django import forms

class CreateNewUser(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input100'}), max_length=50,required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input100'}), max_length=50,required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input100'}), min_length=4, max_length=10,required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input100'}),min_length=4,required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input100'}),min_length=4,required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'input100'}),required=True)


class CheckUser(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input100'}), min_length=4, max_length=10,required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input100'}),min_length=4,required=True)