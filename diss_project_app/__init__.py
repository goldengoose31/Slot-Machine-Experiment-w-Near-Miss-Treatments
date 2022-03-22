from otree.api import *
import random

doc = """
A slot machine experiment to test the saliency of near-miss events
"""


class C(BaseConstants):
    NAME_IN_URL = 'diss_project_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    endowment = 100
    tuple_control_treatment0 = (
        "777", "777", "WWW", "WWW", "WWW",
        "WWW", "PPP", "PPP", "PPP", "PPP",
        "PPP", "PPP", "7P7", "PWP", "WWP",
        "PW7", "P7W", "WP7", "W7P", "7PW",
        "7WP", "PW7", "WP7", "7PW", "W7P"
    )
    tuple_NSNM_treatment1 = (
        "777", "777", "WWW", "WWW", "WWW",
        "WWW", "PPP", "PPP", "PPP", "PPP",
        "PPP", "PPP", "7P7", "W77", "W7W",
        "PWW", "PWP", "7PP", "7P7", "W77",
        "W7W", "PWW", "7PP", "PW7", "7PW"
    )
    tuple_SNM_treatment2 = (
        "777", "777", "WWW", "WWW", "WWW",
        "WWW", "PPP", "PPP", "PPP", "PPP",
        "PPP", "PPP", "77P", "77W", "WWP",
        "WW7", "PPW", "PP7", "77P", "77W",
        "WWP", "WW7", "PP7", "PW7", "WP7"
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # FORM FIELDS
    email_address = models.StringField(label="Please input your email address:")
    consent = models.BooleanField(
        label="Do you consent to your data being used for this experiment?", choices=[
            [True, 'Yes'],
        ])
    understood_instructions = models.BooleanField(
        label="Please confirm you have read and understood the above instructions", choices=[
            [True, 'Yes, I have read and understood'],
        ])
    age = models.IntegerField(label="How old are you?", blank=True)
    gender = models.StringField(
        label="Gender:", blank=True,
        choices=[
            ["male", "Male"],
            ["female", "Female"],
            ["other", "Other"],
            ["prefer_not_to_say", "Prefer not to say"]
        ])
    # EXPERIMENT VARIABLES
    treatment = models.IntegerField()
    slot_shown = models.StringField()
    slot_spun = models.BooleanField()
    tokens = models.IntegerField()
    message = models.StringField()


# FUNCTIONS
def creating_session(subsession):
    for player in subsession.get_players():
        player.treatment = player.id_in_group % 3


# PAGES
class WelcomePage(Page):
    form_model = 'player'
    form_fields = ['consent', 'email_address']


class DemographicsPage(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class InstructionsPage(Page):
    form_model = 'player'
    form_fields = ['understood_instructions']


class FirstSlotsPage(Page):
    form_model = 'player'
    form_fields = ['slot_spun']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.tokens = C.endowment
        if player.treatment == 0:
            slot = random.choice(C.tuple_control_treatment0)
            player.slot_shown = slot + ".png"
            if player.slot_shown == "777.png":
                player.tokens += 40
                player.message = "You won 50 tokens!"
            elif player.slot_shown == "WWW.png":
                player.tokens += 10
                player.message = "You won 20 tokens!"
            elif player.slot_shown == "PPP.png":
                player.tokens += 0
                player.message = "You won 10 tokens!"
            else:
                player.tokens += -10
                player.message = "You lost"
        elif player.treatment == 1:
            slot = random.choice(C.tuple_NSNM_treatment1)
            player.slot_shown = slot + ".png"
            if player.slot_shown == "777.png":
                player.tokens += 40
                player.message = "You won 50 tokens!"
            elif player.slot_shown == "WWW.png":
                player.tokens += 10
                player.message = "You won 20 tokens!"
            elif player.slot_shown == "PPP.png":
                player.tokens += 0
                player.message = "You won 10 tokens!"
            else:
                player.tokens += -10
                player.message = "You lost"
        elif player.treatment == 2:
            slot = random.choice(C.tuple_SNM_treatment2)
            player.slot_shown = slot + ".png"
            if player.slot_shown == "777.png":
                player.tokens += 40
                player.message = "You won 50 tokens!"
            elif player.slot_shown == "WWW.png":
                player.tokens += 10
                player.message = "You won 20 tokens!"
            elif player.slot_shown == "PPP.png":
                player.tokens += 0
                player.message = "You won 10 tokens!"
            else:
                player.tokens += -10
                player.message = "You lost"


class SlotsPage(Page):
    form_model = 'player'
    form_fields = ['slot_spun']

    @staticmethod
    def is_displayed(player):
        return player.tokens != 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.treatment == 0:
            slot = random.choice(C.tuple_control_treatment0)
            player.slot_shown = slot + ".png"
            if player.slot_shown == "777.png":
                player.tokens += 40
                player.message = "You won 50 tokens!"
            elif player.slot_shown == "WWW.png":
                player.tokens += 10
                player.message = "You won 20 tokens!"
            elif player.slot_shown == "PPP.png":
                player.tokens += 0
                player.message = "You won 10 tokens!"
            else:
                player.tokens += -10
                player.message = "You lost"
        elif player.treatment == 1:
            slot = random.choice(C.tuple_NSNM_treatment1)
            player.slot_shown = slot + ".png"
            if player.slot_shown == "777.png":
                player.tokens += 40
                player.message = "You won 50 tokens!"
            elif player.slot_shown == "WWW.png":
                player.tokens += 10
                player.message = "You won 20 tokens!"
            elif player.slot_shown == "PPP.png":
                player.tokens += 0
                player.message = "You won 10 tokens!"
            else:
                player.tokens += -10
                player.message = "You lost"
        elif player.treatment == 2:
            slot = random.choice(C.tuple_SNM_treatment2)
            player.slot_shown = slot + ".png"
            if player.slot_shown == "777.png":
                player.tokens += 40
                player.message = "You won 50 tokens!"
            elif player.slot_shown == "WWW.png":
                player.tokens += 10
                player.message = "You won 20 tokens!"
            elif player.slot_shown == "PPP.png":
                player.tokens += 0
                player.message = "You won 10 tokens!"
            else:
                player.tokens += -10
                player.message = "You lost"


class NoTokensPage(Page):
    pass


    page_sequence = [WelcomePage, DemographicsPage, InstructionsPage, FirstSlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, SlotsPage, NoTokensPage]
