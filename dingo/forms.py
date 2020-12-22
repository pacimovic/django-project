from django import forms

class AddNewFood(forms.Form):
    name = forms.CharField(max_length=20,required=True)
    img = forms.FileField(required=True)
    desc = forms.CharField(widget=forms.Textarea(attrs={'rows' : '7', 'cols' : '100'}),required=True)
    price = forms.CharField(required=True)
    


    