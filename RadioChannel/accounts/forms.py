from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

#My Model
class UserCreateForm(UserCreationForm):
	class Meta():
		model = get_user_model()
		fields = ('username', 'email', 'password1', 'password2')
	def __init__(self, *agrs, **kwargs):
		super().__init__(*agrs, **kwargs)
		self.fields['username'].label = "Username"
		self.fields['email'].label = "Email Address"
