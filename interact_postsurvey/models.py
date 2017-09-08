from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from otree import forms
from django.forms import widgets as django_widgets
#from django.db import models
#from multiselectfields import MultiSelectField

author = 'Chiara Aina'

doc = """
Interact PostSurvey
"""


class Constants(BaseConstants):
    name_in_url = 'interact_postsurvey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

        #
    # def immigrant(self):
    #     self.id_profile = self.participant.vars['id_profile']
    #     self.id_session = self.participant.vars['id_session']
    #     self.id_born    = self.participant.vars['id_born']


    #id_profile = models.PositiveIntegerField(min=1)
    #selected_postsurvey = models.PositiveIntegerField()
    #selected_postsurvey = models.MultiSelectField()

    id_born =  models.PositiveIntegerField(choices=[
            [1,'A Milano'],
            [2,'In Italia, ma non a Milano'],
            [3,'Fuori dall’ Italia'],
            ],
        )

    accomodation = models.PositiveIntegerField(choices=[
    [1,'È in affitto'],
    [2,'È di mia proprietà '],
    [3,'È di mia proprietà e sto pagando il mutuo'],
    [4,'(Non risponde)'],
    ],
    )

    savings = models.PositiveIntegerField(choices=[
    [1,'Risparmiato soldi '],
    [2,'Guadagnato lo stretto necessario'],
    [3,'Usato risparmi messi da parte in precedenza per le necessità quotidiane'],
    [4,'Preso denaro a prestito per le necessità quotidiane'],
    [5,'(Non sa)'],
    [6,'(Non risponde)'],
    ],
    )

    socialclass = models.PositiveIntegerField(choices=[
    [1,'Classe alta'],
    [2,'Classe medio-alta'],
    [3,'Classe medio-bassa'],
    [4,'Classe lavoratrice'],
    [5,'Classe bassa'],
    [6,'(Non sa)'],
    [7,'(Non risponde)'],
    ],
    )

    income = models.PositiveIntegerField(choices=[
    [1,'Meno di 15.000 Euro'],
    [2,'da 15.001 a 20.000 Euro'],
    [3,'da 20.001 a 25.000 Euro'],
    [4,'da 25.001 a 30.000 Euro'],
    [5,'da 30.001 a 35.000 Euro'],
    [6,'da 35.001 a 40.000 Euro'],
    [7,'da 40.001 a 47.000 Euro'],
    [8,'da 47.001 a 58.000 Euro'],
    [9,'da 58.001 a 80.000 Euro'],
    [10,'da 80.001 a 100.000 Euro'],
    [11,'da 100.001 a 150.000 Euro'],
    [12,'oltre 150.000 Euro'],
    [13,'(Non sa)'],
    [14,'(Non risponde)'],
    ],
    )

    religion = models.PositiveIntegerField(choices=[
    [1,'Non sono credente'],
    [2,'Cattolica'],
    [3,'Cristiana (Non cattolica; ad es. Protestante)'],
    [4,'Ebraica'],
    [5,'Musulmana'],
    [6,'Buddista'],
    [7,'Altra religione'],
    [8,'Preferisco non rispondere'],
    ],
    )

    religiosity = models.PositiveIntegerField(choices=[
    [1,'Tutti i giorni'],
    [2,'Più di una volta a settimana'],
    [3,'Una volta alla settimana'],
    [4,'Due-tre volte al mese'],
    [5,'Una volta al mese'],
    [6,'Due-tre volte all’ anno'],
    [7,'Una volta all’ anno'],
    [8,'Mai'],
    [9,'(Non sa)'],
    [10,'(Non risponde)'],
    ],
    )

    dec_asso1 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )
    dec_asso2 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )
    dec_asso3 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )
    dec_asso4 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )
    dec_asso5 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )
    dec_asso6 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )
    dec_asso7 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )
    dec_asso8 = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    takenadvantage = models.PositiveIntegerField(choices=[
    [1,'1, Si la gente cercherebbe di approfittarsi di te'],
    [2,'2'],
    [3,'3'],
    [4,'4'],
    [5,'5'],
    [6,'6'],
    [7,'7'],
    [8,'8'],
    [9,'9'],
    [10,'10, No la gente cercherebbe di compartarsi in modo correto'],
    [11,'(Non sa)'],
    [12,'(Non risponde)'],
    ],
    )

    neighbor1 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor2 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor3 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor4 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor5 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor6 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor7 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor8 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor9 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor10 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    neighbor11 = models.PositiveIntegerField(choices=[
    [1,'OK'],
    [2,'Non vorrei come vicini'],
    ],widget=widgets.RadioSelectHorizontal()
    )

    politics = models.PositiveIntegerField(choices=[
    [1,'Molto'],
    [2,'Abbastanza'],
    [3,'Poco'],
    [4,'Per niente'],
    [5,'(Non sa)'],
    ],
    )

    referendum = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],
    )

    rightleft = models.PositiveIntegerField(choices=[
    [1,'1 Sinistra'],
    [2,'2'],
    [3,'3 Centro Sinistra'],
    [4,'4'],
    [5,'5 Centro'],
    [6,'6'],
    [7,'7 Centro Destra'],
    [8,'8 '],
    [9,'9 Destra'],
    [10,'10'],
    [11,'(Non sa)'],
    [12,'(Non risponde)'],
    ],
    )

    attimm1 = models.PositiveIntegerField(choices=[
    [1,'Molto'],
    [2,'Abbastanza'],
    [3,'Poco'],
    [4,'Per niente'],
    [5,'(Non sa)'],
    ],
    )

    attimm2 = models.PositiveIntegerField(choices=[
    [1,'Molto'],
    [2,'Abbastanza'],
    [3,'Poco'],
    [4,'Per niente'],
    [5,'(Non sa)'],
    ],
    )

    attimm3 = models.PositiveIntegerField(choices=[
    [1,'Molto'],
    [2,'Abbastanza'],
    [3,'Poco'],
    [4,'Per niente'],
    [5,'(Non sa)'],
    ],
    )

    attimm4 = models.PositiveIntegerField(choices=[
    [1,'Molto'],
    [2,'Abbastanza'],
    [3,'Poco'],
    [4,'Per niente'],
    [5,'(Non sa)'],
    ],
    )

    attimm5 = models.PositiveIntegerField(choices=[
    [1,'Molto'],
    [2,'Abbastanza'],
    [3,'Poco'],
    [4,'Per niente'],
    [5,'(Non sa)'],
    ],
    )

    employital = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    [3,'Non si applica']
    ],
    )

    remit = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],
    )

    remitamount = models.PositiveIntegerField(min=1, blank = True)

    discrim = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],
    )

    discrimfreq = models.PositiveIntegerField(choices=[
    [1,'Spesso'],
    [2,'A volte'],
    [3,'Raremente'],
    ],
    )

    discrimtype = models.PositiveIntegerField(choices=[
    [1,'Per strada'],
    [2,'Al lavoro o quando cerco lavoro'],
    [3,'In un negozio, ristorante, o banca'],
    [4,'Quando interagisco con la polizia e le forze dell’ordine'],
    [5,'Altro'],
    ],
    )

    friendsit = models.PositiveIntegerField(choices=[
    [1,'Nessuno'],
    [2,'Uno'],
    [3,'Da 2 a 5'],
    [4,'Da 6 a 10'],
    [5,'Più di 10'],
    ],
    )

    friendsimm = models.PositiveIntegerField(choices=[
    [1,'Nessuno'],
    [2,'Uno'],
    [3,'Da 2 a 5'],
    [4,'Da 6 a 10'],
    [5,'Più di 10'],
    ],
    )

    aquaintit = models.PositiveIntegerField(choices=[
    [1,'Nessuno'],
    [2,'Uno'],
    [3,'Da 2 a 5'],
    [4,'Da 6 a 10'],
    [5,'Più di 10'],
    ],
    )

    aquaintnonit = models.PositiveIntegerField(choices=[
    [1,'Nessuno'],
    [2,'Uno'],
    [3,'Da 2 a 5'],
    [4,'Da 6 a 10'],
    [5,'Più di 10'],
    ],
    )

    meetimm = models.PositiveIntegerField(choices=[
    [1,'Mai'],
    [2,'Raremente'],
    [3,'A volte'],
    [4,'Spesso'],
    [5,'Quasi sempre'],
    ],
    )

    negcontact = models.PositiveIntegerField(choices=[
    [1,'Mai'],
    [2,'Raremente'],
    [3,'A volte'],
    [4,'Spesso'],
    [5,'Quasi sempre'],
    ],
    )

    employimm = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],
    )

    employimmnationality = models.CharField(blank = True)

    colleagues = models.PositiveIntegerField(choices=[
    [1,'Nessuno'],
    [2,'Uno'],
    [3,'Da 2 a 5'],
    [4,'Da 6 a 10'],
    [5,'Più di 10'],
    ],
    )

    knowingsomeone = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],
    )

    ingroupknowledge = models.PositiveIntegerField(choices=[
    [1,'Si'],
    [2,'No'],
    ],
    )

    difficult = models.PositiveIntegerField(choices=[
    [1,'Molto difficile'],
    [2,'Abbastanza difficile'],
    [3,'Non molto difficile'],
    [4,'Per nulla difficile'],
    [5,'(Non risponde)'],
    ],
    )

    contact = models.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 70}),
        verbose_name="",
        max_length=100, blank=True, default=''
    )

    def pass_variables(self):
        self.participant.vars['accomodation'] = self.accomodation
        self.participant.vars['savings'] = self.savings
        self.participant.vars['socialclass'] = self.socialclass
        self.participant.vars['income'] = self.income
        self.participant.vars['religion'] = self.religion
        self.participant.vars['religiosity'] = self.religiosity
        self.participant.vars['dec_asso1'] = self.dec_asso1
        self.participant.vars['takenadvantage'] = self.takenadvantage
        self.participant.vars['neighbor1'] = self.neighbor1
        self.participant.vars['neighbor2'] = self.neighbor2
        self.participant.vars['neighbor3'] = self.neighbor3
        self.participant.vars['neighbor4'] = self.neighbor4
        self.participant.vars['neighbor5'] = self.neighbor5
        self.participant.vars['neighbor6'] = self.neighbor6
        self.participant.vars['neighbor7'] = self.neighbor7
        self.participant.vars['neighbor8'] = self.neighbor8
        self.participant.vars['neighbor9'] = self.neighbor9
        self.participant.vars['neighbor10'] = self.neighbor10
        self.participant.vars['neighbor10'] = self.neighbor11
        self.participant.vars['politics'] = self.politics
        self.participant.vars['referendum'] = self.referendum
        self.participant.vars['rightleft'] = self.rightleft
        self.participant.vars['contact'] = self.contact
        self.participant.vars['attimm1'] = self.attimm1
        self.participant.vars['attimm2'] = self.attimm2
        self.participant.vars['attimm3'] = self.attimm3
        self.participant.vars['attimm4'] = self.attimm4
        self.participant.vars['attimm5'] = self.attimm5
        self.participant.vars['employital'] = self.employital
        self.participant.vars['remit'] = self.remit
        self.participant.vars['remitamount'] = self.remitamount
        self.participant.vars['discrim'] = self.discrim
        self.participant.vars['discrimfreq'] = self.discrimfreq
        self.participant.vars['discrimtype'] = self.discrimtype
        self.participant.vars['friendit'] = self.friendsit
        self.participant.vars['friendsimm'] = self.friendsimm
        self.participant.vars['aquaintit'] = self.aquaintit
        self.participant.vars['aquaintnonit'] = self.aquaintnonit
        self.participant.vars['meetimm'] = self.meetimm
        self.participant.vars['negcontact'] = self.negcontact
        self.participant.vars['employimm'] = self.employimm
        self.participant.vars['employimmnationality'] = self.employimmnationality
        self.participant.vars['colleagues'] = self.colleagues
        self.participant.vars['knowingsomeone'] = self.knowingsomeone
        self.participant.vars['ingroupknowledge'] = self.ingroupknowledge
        self.participant.vars['dfficult'] = self.difficult
