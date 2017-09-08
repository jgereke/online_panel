from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class PostSurvey1_IT(Page):
    form_model = models.Player
    form_fields = ['accomodation','savings', 'socialclass', 'income' ]

def get_form_fields(self):
    return [
            "accomodation",
            "savings",
            "socialclass",
            "income",
            ]

class PostSurvey2_IT(Page):
    form_model = models.Player
    form_fields = ['religion','religiosity']

def get_form_fields(self):
    return ["religion",
            "religiosity",
            ]

class PostSurvey3a_IT(Page):
    form_model = models.Player
    form_fields = ['dec_asso1', 'dec_asso2', 'dec_asso3', 'dec_asso4','dec_asso5', 'dec_asso6', 'dec_asso7', 'dec_asso8' ]

    def before_next_page(self):
        self.player.po_association = self.player.dec_asso1
        self.player.pass_variables()

class PostSurvey3_IT(Page):
    form_model = models.Player
    form_fields = ['takenadvantage', 'neighbor1', 'neighbor2', 'neighbor3', 'neighbor4', 'neighbor5', 'neighbor6', 'neighbor7','neighbor8','neighbor9','neighbor10', 'neighbor11']

def get_form_fields(self):
    return ["takenadvantage"]

def vars_for_template(self):
    return {"neighbor1",
            "neighbor2",
            "neighbor3",
            "neighbor4",
            "neighbor5",
            "neighbor6",
            "neighbor7",
            "neighbor8",
            "neighbor9",
            "neighbor10",
            "neighbor11",
            }

class PostSurvey4a_IT(Page):
    form_model = models.Player
    form_fields = ['politics', 'rightleft']

    def get_form_fields(self):
        return ["politics",
                "rightleft",
                ]

class PostSurvey4b_IT(Page):

    form_model = models.Player
    form_fields = ['referendum']

    def get_form_fields(self):
        return ["referendum",
                ]

    def is_displayed(self):
        return self.participant.vars['id_born'] != 3

class PostSurvey5a_IT(Page):

    form_model = models.Player
    form_fields = ['attimm1','attimm2', 'attimm3','attimm4','attimm5']

    def get_form_fields(self):
        return ["attimm1",
                "attimm2",
                "attimm3",
                "attimm4",
                "attimm5",
                ]

    def is_displayed(self):
        return self.participant.vars['id_born'] != 3

class PostSurvey5b_IT(Page):

    def is_displayed(self):
        return self.participant.vars['id_born'] == 3

    form_model = models.Player
    form_fields = ['remit', 'remitamount']

# passes the variable 'eligible' to all players
    #def vars_for_all_templates(self):
    #    return {'eligible': preselection(self.player)}


    def get_form_fields(self):
        return [
                "remit",
                "remitamount",
                ]

class PostSurvey5c_IT(Page):
    form_model = models.Player
    form_fields = ['discrim']

    def is_displayed(self):
        return self.participant.vars['id_born'] == 3

    def get_form_fields(self):
        return ["discrim"
                ]

class PostSurvey5d_IT(Page):
    form_model = models.Player
    form_fields = ['discrimfreq','discrimtype']

    def get_form_fields(self):
        return [ "employimmnationality",
                ]

    def is_displayed(self):
        return self.player.employimm==1

    def get_form_fields(self):
        return ["discrimfreq",
                "discrimtype",
                ]
    def is_displayed(self):
            return self.player.discrim==1

class PostSurvey6a_IT(Page):
    form_model = models.Player
    form_fields = ['friendsimm','aquaintnonit', 'meetimm']

    def get_form_fields(self):
        return ["friendsimm",
                "aquaintnonit",
                "meetimm",
                ]

    def is_displayed(self):
        return self.participant.vars['id_born'] != 3

class PostSurvey6b_IT(Page):
    form_model = models.Player
    form_fields = ['negcontact','employimm','colleagues']

    def get_form_fields(self):
        return ["negcontact",
                "employimm",
                "colleagues",
                ]

    def is_displayed(self):
        return self.participant.vars['id_born'] != 3


class PostSurvey6c_IT(Page):
    form_model = models.Player
    form_fields = ['employimmnationality']

    def get_form_fields(self):
        return [ "employimmnationality",
                ]

    def is_displayed(self):
        return self.player.employimm==1

class PostSurvey7_IT(Page):
    form_model = models.Player
    form_fields = ['employital','friendsit','aquaintit']

    def get_form_fields(self):
        return ["friendsit",
                "aquaintit",
                "employital"
                ]

    def is_displayed(self):
        return self.participant.vars['id_born'] == 3

class PostSurvey8_IT(Page):
    form_model = models.Player
    form_fields = ['knowingsomeone','ingroupknowledge', 'difficult', 'contact']

    def get_form_fields(self):
        return ["knowingsomeone",
                "ingroupknowledge",
                "difficult",
                "contact",
                ]

page_sequence = [
    PostSurvey1_IT,
    PostSurvey2_IT,
    PostSurvey3a_IT,
    PostSurvey3_IT,
    PostSurvey4a_IT,
    PostSurvey4b_IT,
    PostSurvey5a_IT,
    PostSurvey5b_IT,
    PostSurvey5c_IT,
    PostSurvey5d_IT,
    PostSurvey6a_IT,
    PostSurvey6b_IT,
    PostSurvey6c_IT,
    PostSurvey7_IT,
    PostSurvey8_IT,
]
