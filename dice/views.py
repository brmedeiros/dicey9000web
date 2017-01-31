from django.shortcuts import render

from .forms import HomeDiceRollForm
from .models import DiceRoll

# def home(request):
#     return render(request, 'dice/home.html')

def home(request):
    if request.method == 'POST':
        form = HomeDiceRollForm(request.POST)
        roll_output = ''
        if form.is_valid():
            number_of_dice = form.clean_number_of_dice()
            dice_type = form.clean_dice_type()
            roll_modifier = form.clean_roll_modifier()
            explode_value = form.clean_explode_value()
            success_condition = form.clean_success_condition()
            roll = DiceRoll(number_of_dice, dice_type, roll_modifier, 
                            explode_value, success_condition)
            roll.roll_dice()
            roll.explode_dice()
            roll.success_counter()
            roll_output = roll.output()
        return render(request, 'dice/home.html', {
            'form': form,
            'roll_output': roll_output,
        })
        
            
    else:
        form = HomeDiceRollForm()
        return render(request, 'dice/home.html', {'form': form})
   
