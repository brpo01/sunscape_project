from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

class UsernameMaxAdapter(DefaultAccountAdapter):
    def clean_username(self, username):
        if len(username) > 15:
            raise ValidationError('Please enter a username value less than the current one')
        return DefaultAccountAdapter.clean_username(self,username)