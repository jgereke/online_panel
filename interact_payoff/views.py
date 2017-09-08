from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Overview(Page):
    def before_next_page(self):
        self.player.init_var()

class Payoff_overview_IT(Page):

    form_model = models.Player
    form_fields = ['paid_individual_task']

    def vars_for_template(self):
        return {
            'dec_dg1': self.participant.vars['dec_dg1'],
            'po_dg1': self.participant.vars['po_dg1'],
            'dec_dg2': self.participant.vars['dec_dg2'],
            'po_dg2': self.participant.vars['po_dg2'],
            'dec_svoc': self.participant.vars['dec_svoc'],
            'po_svoc': self.participant.vars['po_svoc'],
            'dec_svonc': self.participant.vars['dec_svonc'],
            'po_svonc': self.participant.vars['po_svonc'],
            'dec_pdguess': self.participant.vars['dec_pdguess'],
            'po_pdguess': self.participant.vars['po_pdguess'],
            'dec_pd1': self.participant.vars['dec_pd1'],
            'po_pd1': self.participant.vars['po_pd1'],
            'dec_pd2': self.participant.vars['dec_pd2'],
            'po_pd2': self.participant.vars['po_pd2'],
            'dec_trustjob': self.participant.vars['dec_trustjob'],
            'po_trustjob': self.participant.vars['po_trustjob'],
            'dec_trustactivity': self.participant.vars['dec_trustactivity'],
            'po_trustact': self.participant.vars['po_trustact'],
            'dec_threat': self.participant.vars['dec_threat'],
            'po_threat': self.participant.vars['po_threat'],
            'dec_donate1': self.participant.vars['dec_donate1'],
            'po_donation': self.participant.vars['po_donation'],
            'dec_infosell': self.participant.vars['dec_infosell'],
            'po_infosell': self.participant.vars['po_infosell'],
            'dec_infobuy': self.participant.vars['dec_infobuy'],
            'po_infobuy': self.participant.vars['po_infobuy'],
        }


class IT_WaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.select_paid_it()


class Payoff_overview_PGG(Page):

    form_model = models.Player
    form_fields = ['paid_pgg']

    def vars_for_template(self):
        return {
            'pgg_1': self.participant.vars['pgg_1'],
            'pgg_2': self.participant.vars['pgg_2'],
            'pgg_3': self.participant.vars['pgg_3'],
            'pgg_4': self.participant.vars['pgg_4'],
            #'pgg_5': self.participant.vars['pgg_5'],
            #'pgg_6': self.participant.vars['pgg_6'],
            #'pgg_7': self.participant.vars['pgg_7'],
            #'pgg_8': self.participant.vars['pgg_8'],
        }


class PGG_WaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.select_paid_pgg()


class Results_IT(Page):
    pass


page_sequence = [
    #Overview,
    Payoff_overview_IT,
    IT_WaitPage,
    Payoff_overview_PGG,
    PGG_WaitPage,
    Results_IT
]
