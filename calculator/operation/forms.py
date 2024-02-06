from django import forms




    # django forms
        # <forms> which predefined in django using the widgets of html(label,input type,button)         
        # # form.charfield()
        # form.booleanfield()
        # emailfield()
        # floatfield()
class Formname(forms.Form):
    name =forms.CharField()
    email = forms.EmailField()