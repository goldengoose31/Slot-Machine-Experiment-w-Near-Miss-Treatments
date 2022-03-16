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
        "777.png", "777.png", "WWW.png", "WWW.png", "WWW.png",
        "WWW.png", "PPP.png", "PPP.png", "PPP.png", "PPP.png",
        "PPP.png", "PPP.png", "7P7.png", "PWP.png", "WWP.png",
        "PW7.png", "P7W.png", "WP7.png", "W7P.png", "7PW.png",
        "7WP.png", "PW7.png", "WP7.png", "7PW.png", "W7P.png"
    )
    tuple_NSNM_treatment2 = (
        "777.png", "777.png", "WWW.png", "WWW.png", "WWW.png",
        "WWW.png", "PPP.png", "PPP.png", "PPP.png", "PPP.png",
        "PPP.png", "PPP.png", "7P7.png", "W77.png", "W7W.png",
        "PWW.png", "PWP.png", "7PP.png", "7P7.png", "W77.png",
        "W7W.png", "PWW.png", "7PP.png", "PW7.png", "7PW.png"
    )
    tuple_SNM_treatment3 = (
        "777.png", "777.png", "WWW.png", "WWW.png", "WWW.png",
        "WWW.png", "PPP.png", "PPP.png", "PPP.png", "PPP.png",
        "PPP.png", "PPP.png", "77P.png", "77W.png", "WWP.png",
        "WW7.png", "PPW.png", "PP7.png", "77P.png", "77W.png",
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
    @staticmethod
    def vars_for_template(player):
        slot = random.choice(C.tuple_control_treatment1)
        player.slot_shown = slot
        return dict(
            image_path="{}".format(slot)
        )


page_sequence = [WelcomePage, DemographicsPage, InstructionsPage, SlotsPage]
