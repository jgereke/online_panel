from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils import timezone
import time
from datetime import datetime, timedelta
from django.utils.timezone import activate


## ENGLISH VERSION

class Task1_instructions(Page):

    def before_next_page(self):
        self.player.random_var()

class Task1_A(Page):

    form_model = models.Player
    form_fields = ['dec_dg1']

    #if html input: error message not displayed
    def error_message(self, values):
        if values['dec_dg1'] > 10 or values['dec_dg1']< 0:
            return 'Controlla la tua risposta: deve essere maggiore di 0 e minore di 10.'

    def vars_for_template(self):
        return {
            'dg_name1': Constants.dg_name1[self.player.id_profile],
            'dg_gen1':  Constants.dg_gen1[self.player.id_profile],
            'dg_age1':  Constants.dg_age1[self.player.id_profile],
            'dg_place1': Constants.dg_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pdg1()

class Task1_B(Page):

    form_model = models.Player
    form_fields = ['dec_dg2']

    def error_message(self, values):
        if values['dec_dg2'] > 10 or values['dec_dg2']< 0:
            return 'Controlla la tua risposta: deve essere maggiore di 0 e minore di 10.'

    def vars_for_template(self):
        return {
            'dg_name2': Constants.dg_name2[self.player.id_profile],
            'dg_gen2': Constants.dg_gen2[self.player.id_profile],
            'dg_age2': Constants.dg_age2[self.player.id_profile],
            'dg_place2': Constants.dg_place2[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pdg2()

class Task2_instructions(Page):
    pass

class Task2(Page):
    form_model = models.Player
    form_fields = ['dec_svoc', 'dec_svonc']

    def before_next_page(self):
        self.player.def_po_svo()

class Task3_instructions(Page):
    pass

class Task3_choice(Page):
    form_model = models.Player
    form_fields = ['dec_pdguess','dec_pdcertain']

    def vars_for_template(self):
        return {
            'pd_name1': Constants.pd_name1[self.player.id_profile],
            'pd_gen1': Constants.pd_gen1[self.player.id_profile],
            'pd_age1': Constants.pd_age1[self.player.id_profile],
            'pd_place1': Constants.pd_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pdguess()

# class Task3_guess(Page):
#     form_model = models.Player
#     form_fields = ['dec_pdcertain']

class Task4(Page):
    form_model = models.Player
    form_fields = ['dec_pd1']

    def vars_for_template(self):
        return {
            'pd_name1': Constants.pd_name1[self.player.id_profile],
            'pd_gen1': Constants.pd_gen1[self.player.id_profile],
            'pd_age1': Constants.pd_age1[self.player.id_profile],
            'pd_place1': Constants.pd_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pd1()

class Task5(Page):
    form_model = models.Player
    form_fields = ['dec_infosell']

    def vars_for_template(self):
        return {
            'pd_name1': Constants.pd_name1[self.player.id_profile],
            'pd_gen1': Constants.pd_gen1[self.player.id_profile],
            'pd_age1': Constants.pd_age1[self.player.id_profile],
            'pd_place1': Constants.pd_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.po_infosell = -float(Constants.pd_infosell) if self.player.dec_infosell=="Si" else 0


class Task6_a1(Page):
    form_model = models.Player
    form_fields = ['dec_infobuy']

    def vars_for_template(self):
        return {
            'pd_name2': Constants.pd_name2[self.player.id_profile],
            'pd_gen2': Constants.pd_gen2[self.player.id_profile],
            'pd_age2': Constants.pd_age2[self.player.id_profile],
            'pd_place2': Constants.pd_place2[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_infobuy()

class Task6_a2(Page):
    form_model = models.Player
    form_fields = ['dec_pd2']

    def vars_for_template(self):
        return {
            'pd_name2': Constants.pd_name2[self.player.id_profile],
            'pd_gen2': Constants.pd_gen2[self.player.id_profile],
            'pd_age2': Constants.pd_age2[self.player.id_profile],
            'pd_place2': Constants.pd_place1[self.player.id_profile],
            'pd_altdec2': Constants.pd_altdec2[self.player.id_profile],
        }

    def before_next_page(self):
        self.player.def_po_infobuy(),
        self.player.def_po_pd2()


class Task6_b1_instructions(Page):
    pass



class Task6_b2(Page):
    form_model = models.Player
    form_fields = ['dec_trustjob']

    def vars_for_template(self):
        return {
            'trust_name1': Constants.trust_name1[self.player.id_profile],
            'trust_gen1': Constants.trust_gen1[self.player.id_profile],
            'trust_age1': Constants.trust_age1[self.player.id_profile],
            'trust_place1': Constants.trust_place1[self.player.id_profile],
            'trust_job': Constants.trust_job[self.player.id_profile],
        }

    def before_next_page(self):
        self.player.po_trustjob = (10-float(self.player.dec_trustjob)) + float(self.player.dec_trustjob)*3*float(Constants.trust_altdec1[self.player.id_profile])


class Task6_b3(Page):
    form_model = models.Player
    form_fields = ['dec_trustcheckjob','dec_trustestimjob']

    def vars_for_template(self):
        return {
            'trust_name1': Constants.trust_name1[self.player.id_profile],
            'trust_gen1': Constants.trust_gen1[self.player.id_profile],
            'dec_trustjob': self.player.dec_trustjob,
        }


class Task6_c1(Page):
    form_model = models.Player
    form_fields = ['dec_trustactivity']

    def vars_for_template(self):
        return {
            'trust_name2': Constants.trust_name2[self.player.id_profile],
            'trust_gen2': Constants.trust_gen2[self.player.id_profile],
            'trust_age2': Constants.trust_age2[self.player.id_profile],
            'trust_place2': Constants.trust_place2[self.player.id_profile],
            'trust_activity': Constants.trust_activity[self.player.id_profile],
        }

    def before_next_page(self):
        self.player.po_trustact = (10-float(self.player.dec_trustactivity)) + float(self.player.dec_trustactivity)*3*float(Constants.trust_altdec2[self.player.id_profile])


class Task6_c2(Page):
    form_model = models.Player
    form_fields = ['dec_trustcheckact','dec_trustestimact']

    def vars_for_template(self):
        return {
            'trust_name2': Constants.trust_name2[self.player.id_profile],
            'trust_gen2': Constants.trust_gen2[self.player.id_profile],
            'dec_trustactivity': self.player.dec_trustactivity,
        }


class Task7_instructionsA(Page):
    pass

class Task7_instructionsB(Page):
    pass

class Task7(Page):
    form_model = models.Player
    form_fields = ['dec_threat']

    def vars_for_template(self):
        return {
            'threat_name': Constants.threat_name[self.player.id_profile],
            'threat_gen': Constants.threat_gen[self.player.id_profile],
            'threat_age': Constants.threat_age[self.player.id_profile],
            'threat_place': Constants.threat_place[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_threat()


class Payoff_overview(Page):
    pass



## ITALIAN VERSION

# def preselection_im():
#     if self.participant.vars['id_born'] == 3:
#         return True
#     else:
#         return False
#
# def preselection_online():
#     if self.participant.vars['id_born'] != 3:
#         return True
#     else:
#         return False
#
# def preselection_onlinenotmilan():
#     if self.participant.vars['id_born'] == 2:
#         return True
#     else:
#         return False

# def preselection_children():
#     if player.children!=1:
#         return True
#     else:
#         return False


class PreSurvey_online(Page):
    form_model = models.Player
    form_fields = ['years_in_milan','quartiere', 'remain_in_milan', 'id_born', 'region']

    def get_form_fields(self):
        return ["years_in_milan",
                "quartiere",
                "remain_in_milan",
                "id_born"]

    def before_next_page(self):
        self.player.permanent_var()


class PreSurvey0_online(Page):
    form_model = models.Player
    form_fields = ['region']

    def get_form_fields(self):
            return ["region",
                ]

    def is_displayed(self):
        return self.participant.vars['id_born'] == 2

class PreSurvey1_online(Page):
    form_model = models.Player
    form_fields = ['country', 'time_in_onlinealy', 'citizenship', 'language', 'italian_knowledge']

    def is_displayed(self):
        return self.participant.vars['id_born'] == 3

    def get_form_fields(self):
        return ["country",
                "time_in_onlinealy",
                "citizenship",
                "language",
                "italian_knowledge",
                ]

class PreSurvey2_online(Page):
    form_model = models.Player
    form_fields = ['married','children', 'household']

    def get_form_fields(self):
        return ["married",
                "children",
                "household",
                ]


class PreSurvey3_online(Page):
    form_model = models.Player
    form_fields = ['wallet', 'dec_risk']

    def get_form_fields(self):
        return ["wallet",
                "dec_risk",
                ]

class Benvenuta_online(Page):
    pass

class Informed_consent_online(Page):
    pass

class Istruzioni_generali_online(Page):

    def before_next_page(self):
        self.player.starttime_questionnaire = timezone.now() + timezone.timedelta(hours=2)
        self.player.starttime_task1 = timezone.now() + timezone.timedelta(hours=2)


class Task1_instructions_online(Page):

    def before_next_page(self):
        self.player.init_var()

class Task1_A_online(Page):

    form_model = models.Player
    form_fields = ['dec_dg1']

    #if html input: error message not displayed
    def error_message(self, values):
        if values['dec_dg1'] > 10 or values['dec_dg1']< 0:
            return 'Controlla la tua risposta: deve essere maggiore di 0 e minore di 10.'

    def vars_for_template(self):
        return {
            'dg_name1': Constants.dg_name1[self.player.id_profile],
            'dg_gen1':  Constants.dg_gen1[self.player.id_profile],
            'dg_age1':  Constants.dg_age1[self.player.id_profile],
            'dg_place1': Constants.dg_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pdg1()

class Task1_B_online(Page):

    form_model = models.Player
    form_fields = ['dec_dg2']

    def error_message(self, values):
        if values['dec_dg2'] > 10 or values['dec_dg2']< 0:
            return 'Controlla la tua risposta: deve essere maggiore di 0 e minore di 10.'

    def vars_for_template(self):
        return {
            'dg_name2': Constants.dg_name2[self.player.id_profile],
            'dg_gen2': Constants.dg_gen2[self.player.id_profile],
            'dg_age2': Constants.dg_age2[self.player.id_profile],
            'dg_place2': Constants.dg_place2[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pdg2()
        self.player.starttime_task2 = timezone.now() + timezone.timedelta(hours=2)

class Task2_instructions_online(Page):
    pass

class Task2_online(Page):
    form_model = models.Player
    form_fields = ['dec_svoc', 'dec_svonc']

    def before_next_page(self):
        self.player.def_po_svo()
        self.player.starttime_task3 = timezone.now() + timezone.timedelta(hours=2)

class Task3_instructions_online(Page):
    pass

class Task3A_choice_online(Page):
    form_model = models.Player
    form_fields = ['dec_pdguess','dec_pdcertain']

    def vars_for_template(self):
        return {
            'pd_name1': Constants.pd_name1[self.player.id_profile],
            'pd_gen1': Constants.pd_gen1[self.player.id_profile],
            'pd_age1': Constants.pd_age1[self.player.id_profile],
            'pd_place1': Constants.pd_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pdguess()

# class Task3_guess(Page):
#     form_model = models.Player
#     form_fields = ['dec_pdcertain']

class Task3B_online(Page):
    form_model = models.Player
    form_fields = ['dec_pd1']

    def vars_for_template(self):
        return {
            'pd_name1': Constants.pd_name1[self.player.id_profile],
            'pd_gen1': Constants.pd_gen1[self.player.id_profile],
            'pd_age1': Constants.pd_age1[self.player.id_profile],
            'pd_place1': Constants.pd_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_pd1()

class Task3C_online(Page):
    form_model = models.Player
    form_fields = ['dec_infosell']

    def vars_for_template(self):
        return {
            'pd_name1': Constants.pd_name1[self.player.id_profile],
            'pd_gen1': Constants.pd_gen1[self.player.id_profile],
            'pd_age1': Constants.pd_age1[self.player.id_profile],
            'pd_place1': Constants.pd_place1[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.po_infosell = -float(Constants.pd_infosell) if self.player.dec_infosell=="Si" else 0


class Task3D_online(Page):
    form_model = models.Player
    form_fields = ['dec_infobuy']

    def vars_for_template(self):
        return {
            'pd_name2': Constants.pd_name2[self.player.id_profile],
            'pd_gen2': Constants.pd_gen2[self.player.id_profile],
            'pd_age2': Constants.pd_age2[self.player.id_profile],
            'pd_place2': Constants.pd_place2[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_infobuy()

class Task3E_online(Page):
    form_model = models.Player
    form_fields = ['dec_pd2']

    def vars_for_template(self):
        return {
            'pd_name2': Constants.pd_name2[self.player.id_profile],
            'pd_gen2': Constants.pd_gen2[self.player.id_profile],
            'pd_age2': Constants.pd_age2[self.player.id_profile],
            'pd_place2': Constants.pd_place1[self.player.id_profile],
            'pd_altdec2': Constants.pd_altdec2[self.player.id_profile],
        }

    def before_next_page(self):
        self.player.def_po_infobuy(),
        self.player.def_po_pd2()
        self.player.starttime_task4 = timezone.now() + timezone.timedelta(hours=2)


class Task4_instructions_online(Page):
    pass



class Task4A_online(Page):
    form_model = models.Player
    form_fields = ['dec_trustjob']

    def vars_for_template(self):
        return {
            'trust_name1': Constants.trust_name1[self.player.id_profile],
            'trust_gen1': Constants.trust_gen1[self.player.id_profile],
            'trust_age1': Constants.trust_age1[self.player.id_profile],
            'trust_place1': Constants.trust_place1[self.player.id_profile],
            'trust_job': Constants.trust_job[self.player.id_profile],
        }

    def before_next_page(self):
        self.player.def_po_trustjob()

class Task4B_online(Page):
    form_model = models.Player
    form_fields = ['dec_trustcheckjob','dec_trustestimjob']

    def vars_for_template(self):
        return {
            'trust_name1': Constants.trust_name1[self.player.id_profile],
            'trust_gen1': Constants.trust_gen1[self.player.id_profile],
            'dec_trustjob': self.player.dec_trustjob,
        }


class Task4C_online(Page):
    form_model = models.Player
    form_fields = ['dec_trustactivity']

    def vars_for_template(self):
        return {
            'trust_name2': Constants.trust_name2[self.player.id_profile],
            'trust_gen2': Constants.trust_gen2[self.player.id_profile],
            'trust_age2': Constants.trust_age2[self.player.id_profile],
            'trust_place2': Constants.trust_place2[self.player.id_profile],
            'trust_activity': Constants.trust_activity[self.player.id_profile],
        }

    def before_next_page(self):
        self.player.def_po_trustact()


class Task4D_online(Page):
    form_model = models.Player
    form_fields = ['dec_trustcheckact','dec_trustestimact']

    def vars_for_template(self):
        return {
            'trust_name2': Constants.trust_name2[self.player.id_profile],
            'trust_gen2': Constants.trust_gen2[self.player.id_profile],
            'dec_trustactivity': self.player.dec_trustactivity,
        }

    def before_next_page(self):
        self.player.starttime_task5 = timezone.now() + timezone.timedelta(hours=2)



class Task5_instructionsA_online(Page):
    pass

class Task5_instructionsB_online(Page):
    pass

class Task5_online(Page):
    form_model = models.Player
    form_fields = ['dec_threat']

    def vars_for_template(self):
        return {
            'threat_name': Constants.threat_name[self.player.id_profile],
            'threat_gen': Constants.threat_gen[self.player.id_profile],
            'threat_age': Constants.threat_age[self.player.id_profile],
            'threat_place': Constants.threat_place[self.player.id_profile]
        }

    def before_next_page(self):
        self.player.def_po_threat()
        self.player.starttime_task6 = timezone.now() + timezone.timedelta(hours=2)

class PostSurvey1_online(Page):
    form_model = models.Player
    form_fields = ['accomodation','savings', 'socialclass', 'income' ]

    def get_form_fields(self):
        return [
            "accomodation",
            "savings",
            "socialclass",
            "income",
            ]

class PostSurvey2_online(Page):
    form_model = models.Player
    form_fields = ['attimm1','attimm2', 'attimm3','attimm4','attimm5']

    def get_form_fields(self):
        return ["attimm1",
                "attimm2",
                "attimm3",
                "attimm4",
                "attimm5",
                ]

class PostSurvey3a_online(Page):
     form_model = models.Player
     form_fields = ['friendsimm','aquaintnonit', 'meetimm']

def get_form_fields(self):
    return ["friendsimm",
            "aquaintnonit",
            "meetimm",
            ]

class PostSurvey3b_online(Page):
     form_model = models.Player
     form_fields = ['negcontact','employimm','colleagues']

     def get_form_fields(self):
         return ["negcontact",
                "employimm",
                "colleagues",
                ]

class PostSurvey3c_online(Page):
    form_model = models.Player
    form_fields = ['employimmnationality']

    def get_form_fields(self):
          return ["employimmnationality",
                   ]

class Payoff_overview_online(Page):
    pass




page_sequence = [
    Benvenuta_online,
    Istruzioni_generali_online,
    Informed_consent_online,
    PreSurvey_online,
    PreSurvey0_online,
    PreSurvey1_online,
    PreSurvey2_online,
    PreSurvey3_online,
    Task1_instructions_online,
    Task1_A_online,
    Task1_B_online,
    Task2_instructions_online,
    Task2_online,
    # Task3_instructions_online,
    Task3A_choice_online,
    Task3B_online,
    Task3C_online,
    Task3D_online,
    Task3E_online,
    Task4_instructions_online,
    Task4A_online,
    Task4B_online,
    Task4C_online,
    Task4D_online,
    Task5_instructionsA_online,
    Task5_instructionsB_online,
    Task5_online,
    PostSurvey1_online,
    PostSurvey2_online,
    PostSurvey3a_online,
    PostSurvey3b_online,
    PostSurvey3c_online,
    Payoff_overview_online
]
