# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
from collections import Counter
# </standard imports>

author = 'Chiara Aina'

doc = """
Interact - Payoff Overview
"""


class Constants(BaseConstants):
    name_in_url = 'interact_payoff'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    selected_individual_task = models.PositiveIntegerField()
    selected_pgg = models.PositiveIntegerField()

    def select_paid_it(self):
        self.vote_individual_task = []
        for p in self.get_players():
            self.vote_individual_task.append(p.paid_individual_task)
        data1 = Counter(self.vote_individual_task)
        self.selected_individual_task= data1.most_common(1)[0][0]
        if self.selected_individual_task == 1:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_dg1']
        elif self.selected_individual_task == 2:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_dg2']
        elif self.selected_individual_task == 3:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_svoc']
        elif self.selected_individual_task == 4:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_svonc']
        elif self.selected_individual_task == 5:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_pdguess']
        elif self.selected_individual_task == 6:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_pd1']
        elif self.selected_individual_task == 7:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_pd2']
        elif self.selected_individual_task == 8:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_trustjob']
        elif self.selected_individual_task == 9:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_trustact']
        elif self.selected_individual_task == 10:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_threat']
        else:
            for p in self.get_players():
                p.payoff_individual_task = p.participant.vars['po_donation']


    def select_paid_pgg(self):
        self.vote_pgg = []
        for p in self.get_players():
            self.vote_pgg.append(p.paid_pgg)
        data2 = Counter(self.vote_pgg)
        self.selected_pgg = data2.most_common(1)[0][0]
        if self.selected_pgg == 1:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_1']
        elif self.selected_pgg == 2:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_2']
        elif self.selected_pgg == 3:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_3']
        elif self.selected_pgg == 4:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_4']
        elif self.selected_pgg == 5:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_5']
        elif self.selected_pgg == 6:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_6']
        elif self.selected_pgg == 7:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_7']
        elif self.selected_pgg == 8:
            for p in self.get_players():
                p.payoff_pgg = p.participant.vars['pgg_8']
        for p in self.get_players():
            p.payoff = p.payoff_individual_task + p.payoff_pgg


class Player(BasePlayer):

    id_profile = models.PositiveIntegerField()
    id_session = models.CharField()

    paid_individual_task = models.PositiveIntegerField(min = 0, max = 11 )
    paid_pgg = models.PositiveIntegerField(min = 0, max = 10)

    payoff_individual_task = models.CurrencyField()
    payoff_pgg = models.CurrencyField()


    def init_var(self):
        self.id_profile = self.participant.vars['id_profile']
        self.id_session = self.participant.vars['id_session']
