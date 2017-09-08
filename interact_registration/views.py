from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Registration(Page):
    form_model = models.Player
    form_fields = [
        'id_profile', 'id_session']

    def before_next_page(self):
        self.player.permanent_var()

class Page1_Registration_IT(Page):
    form_model = models.Player
    form_fields = [
        'id_profile', 'id_session']

    def before_next_page(self):
        self.player.permanent_var()

#page_sequence = [
    #Registration,
    #Welcome,
    #General_rules,
    #Survey
#]
page_sequence = [
    Page1_Registration_IT,
]
