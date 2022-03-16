from otree.api import *
import random

doc = """
A slot machine experiment testing saliency of near-miss events to human behaviour
"""


class C(BaseConstants):
    NAME_IN_URL = 'diss_project_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 500
    tuple_control_treatment1 = (
        "777", "777", "WWW", "WWW", "WWW",
        "WWW", "PPP", "PPP", "PPP", "PPP",
        "PPP", "PPP", "7P7", "PWP", "WWP",
        "PW7", "P7W", "WP7", "W7P", "7PW",
        "7WP", "PW7", "WP7", "7PW", "W7P"
    )
    tuple_NSNM_treatment2 = (
        "777", "777", "WWW", "WWW", "WWW",
        "WWW", "PPP", "PPP", "PPP", "PPP",
        "PPP", "PPP", "7P7", "W77", "W7W",
        "PWW", "PWP", "7PP", "7P7", "W77",
        "W7W", "PWW", "7PP", "PW7", "7PW"
    )
    tuple_SNM_treatment3 = (
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
    email_address = models.StringField(label="Please input your email address:")
    consent = models.BooleanField(label="Do you consent to this experiment?", choices=[
        [True, 'Yes, I consent to this experiment'],
    ])
    understood_instructions = models.BooleanField(label="Have you read and understood the above instructions?", choices=[
        [True, 'Yes, I have read and understood the above instructions'],
    ])
    age = models.IntegerField(label="How old are you?", blank=True)
    gender = models.StringField(label="Gender:", blank=True,
    choices=[
        ["male", "Male"],
        ["female", "Female"],
        ["other", "Other"],
        ["prefer_not_to_say", "Prefer not to say"]
    ])
    slot_shown = models.StringField()


# PAGES
class WelcomePage(Page):
    form_model = 'player'
    form_fields = ['consent', 'email_address']
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class DemographicsPage(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class InstructionsPage(Page):
    form_model = 'player'
    form_fields = ['understood_instructions']
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class SlotsPage(Page):
    endowment = 100
    @staticmethod
    def vars_for_template(player):
        slot = random.choice(C.tuple_SNM_treatment3)
        player.slot_shown = slot
        return dict(
            image_path="{}.png".format(slot)
        )


page_sequence = [WelcomePage, DemographicsPage, InstructionsPage, SlotsPage]
