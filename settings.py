import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

#DEBUG = False


#Time zone setting
# TIME_ZONE = 'Europe/Rome' #don't use with Sqrl database - it set's it itself
# USE_TZ = True

ADMIN_USERNAME = 'interact_otree'
ADMIN_PASSWORD = 'otree'

# don't share this with anybody.
# Change this to something unique (e.g. mash your keyboard),
# and then delete this comment.
SECRET_KEY = 'zzzzzzzzzzzzzzzzzzzzzzzzzzz'

PAGE_FOOTER = ''

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')




# ACCESS_CODE_FOR_DEFAULT_SESSION:
# If you have a "default session" set,
# then an access code will be appended to the URL for authentication.
# You can change this as frequently as you'd like,
# to prevent unauthorized server access.

ACCESS_CODE_FOR_DEFAULT_SESSION = 'my_access_code'

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g.€, CAD, GBP, CHF, CNY, JPY
# For online survey
REAL_WORLD_CURRENCY_CODE = 'Points'
USE_POINTS = True

#REAL_WORLD_CURRENCY_CODE = 'EUR'
#USE_POINTS = False


# e.g. en-gb, de-de, it-it, fr-fr.
# see: https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'it'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = []

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            Source code
        </a> for the below games.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Below are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish to create your own variations.
    Click one to learn more and play.
</p>
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'num_bots': 12,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
    'random_start_order': True,
}


SESSION_CONFIGS = [

    {
        'name': 'interact_online_tasks',
        'display_name': "INTERACT Online",
        'num_demo_participants': 1,
        'app_sequence': ['interact_registration',
                         'interact_online_tasks',
                         ]
    },
    
]

ROOM_DEFAULTS = {}

ROOMS = [

    {'name': 'belss',
    'display_name': 'BELSS',
    'participant_label_file': 'belss.txt'
    },
    {'name': 'belss_abg',
    'display_name': 'BELSS_ABG_1',
    'participant_label_file': 'ABG.txt',
    },
    {'name': 'belss_abg2',
     'display_name': 'BELSS_ABG_2',
     'participant_label_file': 'ABG2.txt',
     },
    {'name': 'belss_abg3',
     'display_name': 'BELSS_ABG_3',
     'participant_label_file': 'ABG3.txt',
     },
    {'name': 'belss_abg4',
     'display_name': 'BELSS_ABG_4',
     'participant_label_file': 'ABG4.txt',
     },
    {'name': 'belss_abg5',
     'display_name': 'BELSS_ABG_5',
     'participant_label_file': 'ABG5.txt',
     }
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
