from os import environ

DEBUG = False
SESSION_CONFIGS = [
    dict(
        name='refugee_decision',
        display_name="Refugee Game",
        num_demo_participants=14,
        #app_sequence= ['svotree','ret_typing', 'refugee_decision' ],
        app_sequence= ['Intro', 'svotree', 'svotree_secondary', 'ret_typing_practice', 'ret_typing', 'refugee_decision', 'demographics']
    )

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2133226331992'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

ROOMS = [
    dict(
        name='test_room',
        display_name='Test room',
    ),
]