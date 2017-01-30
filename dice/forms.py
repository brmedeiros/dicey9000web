from django import forms
from django.core.exceptions import ValidationError

# roll_modifier_help_text = 'You can enter "0" in this field '\
#                           'if you want the sum of the roll results '\
#                           'with no modifier'

#the above comment shoud be in a tooltip

class HomeDiceRollForm(forms.Form):
#     my_errors = {
#         'required': 'hi!!',
#         'invalid1': 'explosion!',
#         'invalid2': 'Enter a integer (positive or negative)'
#     }
    
    number_of_dice = forms.IntegerField(min_value=1, max_value=100, label='Number of Dice')
    dice_type = forms.IntegerField(min_value=1, label='Dice Type')
    roll_modifier = forms.IntegerField(required = False, label='Roll Modifier')
    explode_value = forms.IntegerField(required = False, min_value=3, label='Explode Value')
    success_condition = forms.IntegerField(required = False, min_value=1, label='Success Condition')
    
    def clean_number_of_dice(self):
        data = self.cleaned_data['number_of_dice']
        return data
            
    def clean_dice_type(self):
        return self.cleaned_data['dice_type']

    def clean_roll_modifier(self):
        return self.cleaned_data['roll_modifier']
        
    def clean_explode_value(self):
        data = self.cleaned_data['explode_value']
        try:
            if self.cleaned_data['dice_type'] != None and data > self.cleaned_data['dice_type']:
                raise ValidationError('hi!')
        except (KeyError):
            pass
        return data

    def clean_success_condition(self):
        data = self.cleaned_data['success_condition']
        try:
            if self.cleaned_data['dice_type'] != None and data > self.cleaned_data['dice_type']:
                raise ValidationError('hey!')
        except (KeyError):
            pass
        return data
