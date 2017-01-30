from django.shortcuts import render

from .forms import HomeDiceRollForm
from .models import DiceRoll

# def home(request):
#     return render(request, 'dice/home.html')

def home(request):
    # if request.method == 'POST':
    form = HomeDiceRollForm(request.POST)
    if form.is_valid():
        number_of_dice = form.clean_number_of_dice()
        dice_type = form.clean_dice_type()
        roll_modifier = form.clean_roll_modifier()
        explode_value = form.clean_explode_value()
        success_condition = form.clean_success_condition()
        my_roll = DiceRoll(number_of_dice, dice_type,
                           roll_modifier, explode_value, success_condition)
    return render(request, 'dice/home.html', {'form': form})
    # else:
    #     return render(request, 'dice/home.html')
    

#     return render(request, 'dice/home.html', {
#         'number_of_dice': number_of_dice,
#         'dice_type': dice_type,
#         'roll_modifier': roll_modifier,
#         'explode_value': explode_value,
#         'success_condition': success_condition
#     })
