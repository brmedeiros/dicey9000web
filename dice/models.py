from django.db import models

import random

class DiceRoll():

    def __init__(self, number_of_dice, dice_type, roll_modifier, explode_value, success_condition):
        self.number_of_dice = number_of_dice
        self.dice_type = dice_type
        self.roll_modifier = roll_modifier
        self.explode_value = explode_value
        self.success_condition = success_condition
        self.successes = 0

    def roll_dice(self):
        if self.number_of_dice != None:
            self.results = [random.randint(1, self.dice_type) for i in range(self.number_of_dice)]
            self.formated_results = ['{}'.format(result) for result in self.results]
            return self.results

    @property
    def total(self):
        if self.roll_modifier != None:
            return sum(self.results) + self.roll_modifier

    def explode_dice(self):
        if self.explode_value != None:
            for i, result in enumerate(self.results):
                if result >= self.explode_value:
                    self.results[i+1:i+1] = [random.randint(1, self.dice_type)]
                    self.formated_results[i+1:i+1] = ['x.{}'.format(self.results[i+1])]
        return self.results

    def success_counter(self, html=False):
        if self.success_condition != None:
            self.successes = 0
            for i, result in enumerate(self.results):
                if result >= self.success_condition:
                    self.successes += 1
                    if html==False:
                        self.formated_results[i] = '**{}**'.format(self.formated_results[i])
                    elif html==True:
                        self.formated_results[i] = '<b>{}</b>'.format(self.formated_results[i])
        return self.successes

    def output(self, html=False):
        success_msg = ''
        if self.success_condition != None:
            if self.successes == 0:
                success_msg = '\nFailure...'
                if html==True:
                    success_msg = '<br>Failure...'
            elif self.successes == 1:
                success_msg = '\n**1** success!'
                if html==True:
                    success_msg = '<br><b>1</b> success!'
            elif self.successes > 1:
                success_msg = '\n**{}** successes!'.format(self.successes)
                if html==True:
                    success_msg = '<br><b>{}</b> successes!'.format(self.successes)
                                    
        if self.roll_modifier != None:
            if self.roll_modifier > 0:
                return ' + '.join(self.formated_results) + ' + {} = {}'.format(self.roll_modifier, self.total) + success_msg
            elif self.roll_modifier < 0:
                return ' + '.join(self.formated_results) + ' + ({}) = {}'.format(self.roll_modifier, self.total) + success_msg
            else:
                return ' + '.join(self.formated_results) + ' = {}'.format(self.total) + success_msg
        else:
            return '  '.join(self.formated_results) + success_msg
