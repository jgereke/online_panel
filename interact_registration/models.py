from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Chiara Aina'

doc = """
Interact Registration
"""


class Constants(BaseConstants):
    name_in_url = 'interact_registration'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    id_profile = models.PositiveIntegerField(min=1)
    id_session = models.CharField(choices=['A', 'B', 'C', 'D', 'E', 'F'], widget=widgets.RadioSelect())
    # id_born =  models.PositiveIntegerField(choices=[
    #             [1,'A Milano'],
    #             [2,'In Italia, ma non a Milano'],
    #             [3,'Fuori dall’ Italia'],
    #             ],
    #             )

    def permanent_var(self):
        self.participant.vars['id_profile'] = self.id_profile
        self.participant.vars['id_session'] = self.id_session
        # self.participant.vars['id_born']    = self.id_born


    my_country = models.CharField()
    my_gender = models.CharField()
