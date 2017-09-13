from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)

from django.db.migrations.loader import MigrationLoader
from django.db.migrations.autodetector import MigrationAutodetector
from django.utils import timezone

import random



author = 'Johanna Gereke'

doc = """
INTERACT Online Tasks
"""


class Constants(BaseConstants):
    name_in_url = 'interact_online_tasks'
    players_per_group = None
    num_rounds = 1

#Fixed randomization: first position empty, so we can use "id_profile"
    dg_name1=[	' ',	'Anna',	'Mohammed',	'Xi-Wang',	'Antonio',	'Giovanni',	'Maria',	]
    dg_gen1=[	' ',	'She',	'He',	'He',	'He',	'He',	'She',	]
    dg_place1=[	' ',	'Lombardia',	'Marocco',	'Cina',	'Lombardia',	'Lombardia',	'Lombardia',	]
    dg_age1=[	' ',	'56',	'23',	'49',	'31',	'61',	'39',	]
    dg_name2=[	' ',	'Patricia',	'Giovanni',	'Anna',	'Alia',	'Patricia',	'Edenjevy',	]
    dg_gen2=[	' ',	'She',	'He',	'She',	'She',	'She',	'He',	]
    dg_place2=[	' ',	'Filippine',	'Lombardia',	'Lombardia',	'Marocco',	'Filippine',	'Filippine',	]
    dg_age2=[	' ',	'47',	'50',	'56',	'50',	'47',	'49',	]
    pd_name1=[	' ',	'Edenjevy',	'Anna',	'Sandra',	'Xing-Fu',	'Oana',	'Elena',	]
    pd_gen1=[	' ',	'He',	'She',	'She',	'He',	'She',	'She',	]
    pd_place1=[	' ',	'Filippine',	'Lombardia',	'Perù',	'Cina',	'Romania',	'Lombardia',	]
    pd_age1=[	' ',	'49',	'56',	'39',	'41',	'46',	'59',	]
    pd_altdec1=[	' ',	'partecipare',	'non partecipare',	'partecipare',	'partecipare',	'non partecipare',	'partecipare',	]
    pd_name2=[	' ',	'Francesco',	'Sabrina',	'Diego',	'Anis',	'Anna',	'Angelo',	]
    pd_gen2=[	' ',	'He',	'She',	'He',	'He',	'She',	'He',	]
    pd_place2=[	' ',	'Lombardia',	'Marocco',	'Perù',	'Marocco',	'Lombardia',	'Filippine',	]
    pd_age2=[	' ',	'24',	'45',	'52',	'18',	'25',	'46',	]
    pd_altdec2=[	' ',	'partecipare',	'non partecipare',	'non partecipare',	'partecipare',	'non partecipare',	'partecipare',	]
    trust_name1=[	' ',	'Loysa',	'Li Mei',	'Bogdan',	'Antonio',	'Angela',	'Francesco',	]
    trust_gen1=[	' ',	'She',	'She',	'He',	'He',	'She',	'He',	]
    trust_place1=[	' ',	'Filippine',	'Cina',	'Romania',	'Lombardia',	'Filippine',	'Lombardia',	]
    trust_age1=[	' ',	'23',	'40',	'27',	'44',	'23',	'37',	]
    trust_job=[	' ',	'nell’assistenza agli anziani',	'in un supermercato',	'in un supermercato',	'nell’assistenza agli anziani',	'in un supermercato',	'nell’assistenza agli anziani',	]
    trust_altdec1=[	'0',	'0.5',	'0',	'0.6',	'0.5',	'0',	'0',	]
    trust_name2=[	' ',	'Antonio',	'Anas',	'Anis',	'Sabrina',	'Alia',	'Loysa',	]
    trust_gen2=[	' ',	'He',	'He',	'He',	'She',	'She',	'She',	]
    trust_place2=[	' ',	'Lombardia',	'Marocco',	'Marocco',	'Marocco',	'Marocco',	'Filippine',	]
    trust_age2=[	' ',	'44',	'28',	'33',	'45',	'37',	'23',	]
    trust_activity=[	' ',	'e’ un rappresentante dei genitori nella classe di suo figlio.',	'fa volontariato nel campo estivo della Chiesa nel suo quartiere.',	'fa volontariato nel campo estivo della Moschea nel suo quartiere.',	'fa volontariato in un’associazione culturale del Marocco.',	'ama cucinare.',	'e’ un rappresentante dei genitori nella classe di suo figlio.',	]
    trust_altdec2=[	'0',	'0',	'0',	'0.5',	'0',	'0.6',	'0.5',	]
    threat_name=[	' ',	'Melvin',	'Giovanni',	'Fang Hua',	'Elena',	'Francesco',	'Maria',	]
    threat_gen=[	' ',	'He',	'He',	'She',	'She',	'He',	'She',	]
    threat_place=[	' ',	'Filippine',	'Lombardia',	'Cina',	'Lombardia',	'Lombardia',	'Lombardia',	]
    threat_age=[	' ',	'33',	'49',	'30',	'24',	'52',	'52',	]
    threat_altdec=[	' ',	'Prendere',	'Non prendere',	'Prendere',	'Non prendere',	'Prendere',	'Non prendere',	]

        #Other constants to be defined
    cc = 5
    dc = 8
    cd = 1
    dd = 3
    pd_infosell = c(0.50)
    pd_infobuy = c(0.50)
    minimum_age = 18
    maximum_age = 70

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):

    selected_individual_task = models.PositiveIntegerField()
    selected_pgg = models.PositiveIntegerField

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

class Player(BasePlayer):
    id_profile = models.PositiveIntegerField()
    id_session = models.CharField()
    id_born =  models.PositiveIntegerField(choices=[
            [1,'A Milano'],
            [2,'In Italia, ma non a Milano'],
            [3,'Fuori dall’ Italia'],
            ],
        )

    def permanent_var(self):
        self.participant.vars['id_born'] = self.id_born
        #self.participant.vars['id_profile'] = self.id_profile
        #self.participant.vars['id_session'] = self.id_session

    choices = models.CharField(
            widget=widgets.RadioSelect(attrs={'readonly':'readonly'}),
    )

    #Pre Survey Questions
    city = models.CharField()

    residencetime = models.PositiveIntegerField(choices=[
        [1, 'meno di un anno'],
        [2, 'tra 1-3 anni'],
        [3, '4-10 anni'],
        [4, '11-15 anni'],
        [5, '16-20 anni'],
        [6, '21 anni o più'],
        ],
        )


    region = models.CharField()

    married = models.PositiveIntegerField(choices=[
       [1,'Single'],
       [2,'Sposato/a o convinvente'],
       [3,'Vedovo/a'],
       [4,'Separato/a o divorziato/a'],
    ],
    )

    children = models.PositiveIntegerField(choices=[
        [1,'No'],
        [2,'Si, 1 bambina/o'],
        [3,'Si, 2 bambini'],
        [4,'Si, 3 bambini'],
        [5,'Si, 4 bambini o più']
        ],
    )

    household = models.PositiveIntegerField(choices=[
        [1,'Vivo da solo/a'],
        [2,'Siamo in 2'],
        [3,'Siamo in 3'],
        [4,'Siamo in 4'],
        [5,'Siamo in 5'],
        [6,'Siamo in 6'],
        [7,'Siamo 7 o più'],
        ],
    )

    wallet = models.PositiveIntegerField(choices=[
        [1,'Quasi certo'],
        [2,'Molto probabile'],
        [3,'Non molto probabile'],
        [4,'Per nulla probabile'],
        ],
    )

    dec_risk = models.PositiveIntegerField(min=0, max=10)

    accomodation = models.PositiveIntegerField(choices=[
        [1,'È in affitto'],
        [2,'È di mia proprietà '],
        [3,'È di mia proprietà e sto pagando il mutuo'],
        [4,'(Non risponde)'],
        ],
    )

    savings = models.PositiveIntegerField(choices=[
        [1,'Risparmiato soldi'],
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

    friendsimm = models.PositiveIntegerField(choices=[
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

    #Input task
    dec_dg1 = models.PositiveIntegerField(min=0, max=10)
    dec_dg2 = models.PositiveIntegerField(min=0, max=10)
    dec_svoc = models.CharField(choices=['Partecipare', 'Non partecipare'], widget=widgets.RadioSelect())
    dec_svonc = models.CharField(choices=['Partecipare', 'Non partecipare'], widget=widgets.RadioSelect())
    dec_pdguess = models.CharField(choices=['Partecipare', 'Non partecipare'], widget=widgets.RadioSelect())
    dec_pdcertain = models.CharField( choices=['Molto sicuro', 'Abbastanza sicuro', 'Abbastanza incerto', 'Molto incerto'], widget=widgets.RadioSelect())
    dec_pd1 = models.CharField(choices=['Partecipare', 'Non partecipare'], widget=widgets.RadioSelect())
    #dec_infosell = models.CharField(choices=['Si, regardless la sua decisione', 'Si, solo se ha scelto Partecipare', 'Si, solo se ha scelto di Non Partecipare', 'No'], widget=widgets.RadioSelect())
    dec_infosell = models.CharField(choices=['Si', 'No'], widget=widgets.RadioSelect())
    dec_infobuy = models.CharField(choices=['Si', 'No'], widget=widgets.RadioSelect())
    dec_pd2 = models.CharField(choices=['Partecipare', 'Non partecipare'], widget=widgets.RadioSelect())
    dec_trustjob = models.PositiveIntegerField(min=0, max=10)
    #dec_trustjob = models.PositiveIntegerField( choices = [0,1,2,3,4,5,6,7,8,9,10], widget=widgets.RadioSelect(attrs={'class': 'inline'}))
    dec_trustcheckjob = models.PositiveIntegerField(min=0 )
    dec_trustestimjob = models.PositiveIntegerField(min= 0)
    dec_trustactivity = models.PositiveIntegerField(min=0, max=10)
    # dec_trustactivity = models.PositiveIntegerField( choices = [0,1,2,3,4,5,6,7,8,9,10], widget=widgets.RadioSelect(attrs={'class': 'inline'}))
    dec_trustcheckact = models.PositiveIntegerField(min=0 )
    dec_trustestimact = models.PositiveIntegerField(min= 0)
    dec_threat = models.CharField(choices=['Protetto', 'Non protetto'], widget=widgets.RadioSelect())


    #Payoff
    po_dg1 = models.CurrencyField()
    po_dg2 = models.CurrencyField()
    po_svoc = models.CurrencyField()
    po_svonc = models.CurrencyField()
    po_pdguess = models.CurrencyField()
    po_pd1 = models.CurrencyField()
    po_infosell = models.CurrencyField()
    po_infobuy = models.CurrencyField()
    po_pd2 = models.CurrencyField()
    po_trustjob = models.CurrencyField()
    po_trustact = models.CurrencyField()
    po_threat = models.CurrencyField()

    #Timers
    starttime_questionnaire = models.DateTimeField()
    starttime_task1 = models.DateTimeField()
    starttime_task2 = models.DateTimeField()
    starttime_task3 = models.DateTimeField()
    starttime_task4 = models.DateTimeField()
    starttime_task5 = models.DateTimeField()
    starttime_lastpage = models.DateTimeField()

    # Save ID Profile - done with Chiara
    #dg_name1 = models.CharField() # created the variable to be stored
    #dg_name2 = models.CharField()

    #Initialize the variable
    def init_var(self):
        self.id_profile =  self.participant.vars['id_profile']
        self.id_session = self.participant.vars['id_session']
        #self.dg_name1 = Constants.dg_name1[self.player.id_profile]
        #self.dg_name2  = Constants.dg_name2[self.player.id_profile]

    #Assign payoff: at the end condensed in a unique function!
    def def_po_pdg1(self):
        self.po_dg1 = self.dec_dg1

    def def_po_pdg2(self):
        self.po_dg2 = self.dec_dg2

    def def_po_svo(self):
        if self.dec_svoc == "Partecipare":
            self.po_svoc = Constants.cc
        else:
            self.po_svoc = Constants.dc
        if self.dec_svonc == "Partecipare":
            self.po_svonc = Constants.cd
        else:
            self.po_svonc = Constants.dd

    def def_po_pdguess(self):
        if Constants.pd_altdec1[self.id_profile] ==  self.dec_pdguess:
            self.po_pdguess = 8
        else:
            self.po_pdguess = 0

    def def_po_pd1(self):
        if Constants.pd_altdec1[self.id_profile] ==  "Partecipare":
            if self.dec_pd1 == "Partecipare":
                self.po_pd1 = Constants.cc
            else:
                self.po_pd1 = Constants.dc
        else:
            if self.dec_pd1 == "Partecipare":
                self.po_pd1 = Constants.cd
            else:
                self.po_pd1 = Constants.dd

    # def def_po_infosell(self):
    #     pass
    #Write all when we have the actual answer for the question
    #If yes and specific decision: -{{Constants.pd_infosell}}, otherwise: 0

    def def_po_infobuy(self):
        if self.dec_infobuy == "Si":
            self.po_infobuy = -float(Constants.pd_infobuy)
        else:
            self.po_infobuy = 0


    def def_po_trustjob(self):
            self.po_trustjob = (10-float(self.dec_trustjob)) + float(self.dec_trustjob)*3*float(Constants.trust_altdec1[self.id_profile])

    def def_po_trustact(self):
            self.po_trustact = (10-float(self.dec_trustactivity)) + float(self.dec_trustactivity)*3*float(Constants.trust_altdec2[self.id_profile])

    # def def_po_trust1(self):
    #     self.trust_job*3*float(Constants.trust_altdec1[self.id_profile])


    def def_po_pd2(self):
        if Constants.pd_altdec2[self.id_profile] ==  "Partecipare":
            if self.dec_pd2 == "Partecipare":
                self.po_pd2 = Constants.cc
            else:
                self.po_pd2 = Constants.dc
        else:
            if self.dec_pd2 == "Partecipare":
                self.po_pd2 = Constants.cd
            else:
                self.po_pd2 = Constants.dd

    def def_po_threat(self):
        if Constants.threat_altdec[self.id_profile] ==  "Prendere":
            if self.dec_threat == "Non protetto":
                self.po_threat = -3
            else:
                self.po_threat = 0
        else:
            if self.dec_pd2 == "Non protetto":
                self.po_threat = 5
            else:
                self.po_threat = 0

    def pass_variables(self):
        self.participant.vars['dec_dg1'] = self.dec_dg1
        self.participant.vars['po_dg1'] = self.po_dg1
        self.participant.vars['dec_dg2'] = self.dec_dg2
        self.participant.vars['po_dg2'] = self.po_dg2
        self.participant.vars['dec_svoc'] = self.dec_svoc
        self.participant.vars['po_svoc'] = self.po_svoc
        self.participant.vars['dec_svonc'] = self.dec_svonc
        self.participant.vars['po_svonc'] = self.po_svonc
        self.participant.vars['dec_pdguess'] = self.dec_pdguess
        self.participant.vars['po_pdguess'] = self.po_pdguess
        self.participant.vars['dec_pd1'] = self.dec_pd1
        self.participant.vars['po_pd1'] = self.po_pd1
        self.participant.vars['dec_pd2'] = self.dec_pd2
        self.participant.vars['po_pd2'] = self.po_pd2
        self.participant.vars['dec_trustjob'] = self.dec_trustjob
        self.participant.vars['po_trustjob'] = self.po_trustjob
        self.participant.vars['dec_trustactivity'] = self.dec_trustactivity
        self.participant.vars['po_trustact'] = self.po_trustact
        self.participant.vars['dec_threat'] = self.dec_threat
        self.participant.vars['po_threat'] = self.po_threat
        self.participant.vars['dec_infosell'] = self.dec_infosell
        self.participant.vars['po_infosell'] = self.po_infosell
        self.participant.vars['dec_infobuy'] = self.dec_infobuy
        self.participant.vars['po_infobuy'] = self.po_infobuy
        self.participant.vars['quartiere'] = self.quartiere
        #self.participant.vars['born'] = self.born
        self.participant.vars['married'] = self.married
        self.participant.vars['children'] = self.children
        self.participant.vars['household'] = self.household
        self.participant.vars['wallet'] = self.wallet
        self.participant.vars['dec_risk'] = self.dec_risk
        self.participant.vars['accomodation'] = self.accomodation
        self.participant.vars['savings'] = self.savings
        self.participant.vars['socialclass'] = self.socialclass
        self.participant.vars['income'] = self.income
        self.participant.vars['attimm1'] = self.attimm1
        self.participant.vars['attimm2'] = self.attimm2
        self.participant.vars['attimm3'] = self.attimm3
        self.participant.vars['attimm4'] = self.attimm4
        self.participant.vars['attimm5'] = self.attimm5
        self.participant.vars['friendsimm'] = self.friendsimm
        self.participant.vars['aquaintnonit'] = self.aquaintnonit
        self.participant.vars['meetimm'] = self.meetimm
        self.participant.vars['negcontact'] = self.negcontact
        self.participant.vars['employimm'] = self.employimm
        self.participant.vars['employimmnationality'] = self.employimmnationality
        self.participant.vars['colleagues'] = self.colleagues
