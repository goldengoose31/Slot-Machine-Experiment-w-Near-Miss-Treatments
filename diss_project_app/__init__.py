from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'diss_project_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    tuple_control_treatment1 = (
        "https://i.imgur.com/mWPeXFD.png", "https://i.imgur.com/mWPeXFD.png", "https://i.imgur.com/nfOEJxr.png",
        "https://i.imgur.com/nfOEJxr.png", "https://i.imgur.com/nfOEJxr.png", "https://i.imgur.com/nfOEJxr.png",
        "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png",
        "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png",
        "https://i.imgur.com/JoHUCo0.png", "https://i.imgur.com/pRqbgB8.png", "https://i.imgur.com/ss97xZw.png",
        "https://i.imgur.com/M2uLwOi.png", "https://i.imgur.com/2CwpGNc.png", "https://i.imgur.com/2oRnDfO.png",
        "https://i.imgur.com/CCKr5nO.png", "https://i.imgur.com/KDxzOKe.png", "https://i.imgur.com/09VyiAL.png",
        "https://i.imgur.com/M2uLwOi.png", "https://i.imgur.com/2oRnDfO.png", "https://i.imgur.com/KDxzOKe.png",
        "https://i.imgur.com/CCKr5nO.png")
    tuple_NSNM_treatment2 = (
        "https://i.imgur.com/mWPeXFD.png", "https://i.imgur.com/mWPeXFD.png", "https://i.imgur.com/nfOEJxr.png",
        "https://i.imgur.com/nfOEJxr.png", "https://i.imgur.com/nfOEJxr.png", "https://i.imgur.com/nfOEJxr.png",
        "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png",
        "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png",)
    tuple_SNM_treatment3 = (
        "https://i.imgur.com/mWPeXFD.png", "https://i.imgur.com/mWPeXFD.png", "https://i.imgur.com/nfOEJxr.png",
        "https://i.imgur.com/nfOEJxr.png", "https://i.imgur.com/nfOEJxr.png", "https://i.imgur.com/nfOEJxr.png",
        "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png",
        "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png", "https://i.imgur.com/WRc7KkB.png",)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email_address = models.StringField(label="Please input your email address:")
    consent = models.BooleanField(label="Do you consent to this experiment?", choices=[
        [True, 'Yes, I consent to this experiment'],
        [False, 'No, I do not consent to this experiment'],
    ])
    understood_instructions = models.BooleanField(label="Have you read and understood the above instructions?", choices=[
        [True, 'Yes, I have read and understood the above instructions'],
        [False, 'No, I have not read and understood the above instructions'],
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


class DemographicsPage(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class InstructionsPage(Page):
    form_model = 'player'
    form_fields = ['understood_instructions']


class SlotsPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        slot = random.choice(C.tuple_control_treatment1)
        player.slot_shown = slot


page_sequence = [WelcomePage, DemographicsPage, InstructionsPage, SlotsPage]
