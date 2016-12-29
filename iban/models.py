# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

# additional models import / requires "django_iban" to be installed
from django_iban.fields import IBANField , SWIFTBICField

author = 'Felix Albrecht ,Thomas Graeber, Thorben Woelk'

doc = """
Standardized End Page
"""

class Constants(BaseConstants):
    name_in_url = 'endofexperiment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    iban = IBANField(verbose_name="IBAN")

    bic = SWIFTBICField(verbose_name="BIC")

    name = models.CharField(verbose_name="Nachname:",max_length=50)

    vorname = models.CharField(verbose_name="Vorname:", max_length=50)

    street = models.CharField(verbose_name="Straße / Hausnr.:", max_length=50)

    city = models.CharField(verbose_name="Stadt:", max_length=50)

    zipcode = models.IntegerField(verbose_name="PLZ:", max_length=10)
