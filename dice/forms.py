from django import forms
from django.core.exceptions import ValidationError

# roll_modifier_help_text = 'You can enter "0" in this field '\
#                           'if you want the sum of the roll results '\
#                           'with no modifier'

#the above comment shoud be in a tooltip

class HomeDiceRollForm(forms.Form):
    my_errors = {
        'required': 'This field is required',
        'invalid1': 'Enter a postive integer',
        'invalid2': 'Enter a integer (positive or negative)'
    }
    
    number_of_dice = forms.IntegerField(error_messages = my_errors)
    dice_type = forms.IntegerField(error_messages = my_errors)
    roll_modifier = forms.IntegerField(required = False, error_messages = my_errors)
    explode_value = forms.IntegerField(required = False, error_messages = my_errors)
    success_condition = forms.IntegerField(required = False, error_messages = my_errors)

    def clean_number_of_dice(self):
        data = self.cleaned_data['number_of_dice']
        if data < 0:
            raise ValidationError(code='invalid1')
        return data
            
    def clean_dice_type(self):
        data = self.cleaned_data['dice_type']
        if data < 0:
            raise ValidationError(code='invalid1')
        return data

    def clean_roll_modifier(self):
        data = self.cleaned_data['roll_modifier']
        # if data < 0:
        #     raise ValidationError(code='invalid2')
        return data

    def clean_explode_value(self):
        data = self.cleaned_data['explode_value']
        # if data < 0:
        #     raise ValidationError(code='invalid1')
        return data

    def clean_success_condition(self):
        data = self.cleaned_data['success_condition']
        # if data < 0:
        #     raise ValidationError(code='invalid1')
        return data
