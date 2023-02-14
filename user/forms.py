from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label='Kullanici adi')
    password=forms.CharField( max_length=20, label='Parola',widget=forms.PasswordInput) # input yzilanda text kimi deyil,password kimi gorulecek
    confirm=forms.CharField( max_length=20, label='Parolayi dogrula',widget=forms.PasswordInput)


    def clean(self):# clean metodu melumatlarin dogru olub olmadigini yoxlayir
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        confirm=self.cleaned_data.get('confirm')

        if password and confirm and password!=confirm:# eger bu fieldler doldurulubsa ve passwordlar eyni deyilse,awagidaki erroru versin
            raise forms.ValidationError('Parolalar eslesmiyor!')
        values={
            'username': username,
            'password': password
        }
        return values

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,label='Kullanici adi')
    password=forms.CharField(max_length=20, label='Parola',widget=forms.PasswordInput)