#!/usr/bin/env python
# flake8: noqa
# pylint: disable=C0103,C0301,R0903
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2016
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

"""This module contains a object that represents an Emoji."""

from future.utils import bytes_to_native_str as n


class Emoji(object):
    """This object represents an Emoji."""

    GRINNING_FACE_WITH_SMILING_EYES = n(b'\xF0\x9F\x98\x81')
    FACE_WITH_TEARS_OF_JOY = n(b'\xF0\x9F\x98\x82')
    SMILING_FACE_WITH_OPEN_MOUTH = n(b'\xF0\x9F\x98\x83')
    SMILING_FACE_WITH_OPEN_MOUTH_AND_SMILING_EYES = n(b'\xF0\x9F\x98\x84')
    SMILING_FACE_WITH_OPEN_MOUTH_AND_COLD_SWEAT = n(b'\xF0\x9F\x98\x85')
    SMILING_FACE_WITH_OPEN_MOUTH_AND_TIGHTLY_CLOSED_EYES = n(b'\xF0\x9F\x98\x86')
    WINKING_FACE = n(b'\xF0\x9F\x98\x89')
    SMILING_FACE_WITH_SMILING_EYES = n(b'\xF0\x9F\x98\x8A')
    FACE_SAVOURING_DELICIOUS_FOOD = n(b'\xF0\x9F\x98\x8B')
    RELIEVED_FACE = n(b'\xF0\x9F\x98\x8C')
    SMILING_FACE_WITH_HEART_SHAPED_EYES = n(b'\xF0\x9F\x98\x8D')
    SMIRKING_FACE = n(b'\xF0\x9F\x98\x8F')
    UNAMUSED_FACE = n(b'\xF0\x9F\x98\x92')
    FACE_WITH_COLD_SWEAT = n(b'\xF0\x9F\x98\x93')
    PENSIVE_FACE = n(b'\xF0\x9F\x98\x94')
    CONFOUNDED_FACE = n(b'\xF0\x9F\x98\x96')
    FACE_THROWING_A_KISS = n(b'\xF0\x9F\x98\x98')
    KISSING_FACE_WITH_CLOSED_EYES = n(b'\xF0\x9F\x98\x9A')
    FACE_WITH_STUCK_OUT_TONGUE_AND_WINKING_EYE = n(b'\xF0\x9F\x98\x9C')
    FACE_WITH_STUCK_OUT_TONGUE_AND_TIGHTLY_CLOSED_EYES = n(b'\xF0\x9F\x98\x9D')
    DISAPPOINTED_FACE = n(b'\xF0\x9F\x98\x9E')
    ANGRY_FACE = n(b'\xF0\x9F\x98\xA0')
    POUTING_FACE = n(b'\xF0\x9F\x98\xA1')
    CRYING_FACE = n(b'\xF0\x9F\x98\xA2')
    PERSEVERING_FACE = n(b'\xF0\x9F\x98\xA3')
    FACE_WITH_LOOK_OF_TRIUMPH = n(b'\xF0\x9F\x98\xA4')
    DISAPPOINTED_BUT_RELIEVED_FACE = n(b'\xF0\x9F\x98\xA5')
    FEARFUL_FACE = n(b'\xF0\x9F\x98\xA8')
    WEARY_FACE = n(b'\xF0\x9F\x98\xA9')
    SLEEPY_FACE = n(b'\xF0\x9F\x98\xAA')
    TIRED_FACE = n(b'\xF0\x9F\x98\xAB')
    LOUDLY_CRYING_FACE = n(b'\xF0\x9F\x98\xAD')
    FACE_WITH_OPEN_MOUTH_AND_COLD_SWEAT = n(b'\xF0\x9F\x98\xB0')
    FACE_SCREAMING_IN_FEAR = n(b'\xF0\x9F\x98\xB1')
    ASTONISHED_FACE = n(b'\xF0\x9F\x98\xB2')
    FLUSHED_FACE = n(b'\xF0\x9F\x98\xB3')
    DIZZY_FACE = n(b'\xF0\x9F\x98\xB5')
    FACE_WITH_MEDICAL_MASK = n(b'\xF0\x9F\x98\xB7')
    GRINNING_CAT_FACE_WITH_SMILING_EYES = n(b'\xF0\x9F\x98\xB8')
    CAT_FACE_WITH_TEARS_OF_JOY = n(b'\xF0\x9F\x98\xB9')
    SMILING_CAT_FACE_WITH_OPEN_MOUTH = n(b'\xF0\x9F\x98\xBA')
    SMILING_CAT_FACE_WITH_HEART_SHAPED_EYES = n(b'\xF0\x9F\x98\xBB')
    CAT_FACE_WITH_WRY_SMILE = n(b'\xF0\x9F\x98\xBC')
    KISSING_CAT_FACE_WITH_CLOSED_EYES = n(b'\xF0\x9F\x98\xBD')
    POUTING_CAT_FACE = n(b'\xF0\x9F\x98\xBE')
    CRYING_CAT_FACE = n(b'\xF0\x9F\x98\xBF')
    WEARY_CAT_FACE = n(b'\xF0\x9F\x99\x80')
    FACE_WITH_NO_GOOD_GESTURE = n(b'\xF0\x9F\x99\x85')
    FACE_WITH_OK_GESTURE = n(b'\xF0\x9F\x99\x86')
    PERSON_BOWING_DEEPLY = n(b'\xF0\x9F\x99\x87')
    SEE_NO_EVIL_MONKEY = n(b'\xF0\x9F\x99\x88')
    HEAR_NO_EVIL_MONKEY = n(b'\xF0\x9F\x99\x89')
    SPEAK_NO_EVIL_MONKEY = n(b'\xF0\x9F\x99\x8A')
    HAPPY_PERSON_RAISING_ONE_HAND = n(b'\xF0\x9F\x99\x8B')
    PERSON_RAISING_BOTH_HANDS_IN_CELEBRATION = n(b'\xF0\x9F\x99\x8C')
    PERSON_FROWNING = n(b'\xF0\x9F\x99\x8D')
    PERSON_WITH_POUTING_FACE = n(b'\xF0\x9F\x99\x8E')
    PERSON_WITH_FOLDED_HANDS = n(b'\xF0\x9F\x99\x8F')
    BLACK_SCISSORS = n(b'\xE2\x9C\x82')
    WHITE_HEAVY_CHECK_MARK = n(b'\xE2\x9C\x85')
    AIRPLANE = n(b'\xE2\x9C\x88')
    ENVELOPE = n(b'\xE2\x9C\x89')
    RAISED_FIST = n(b'\xE2\x9C\x8A')
    RAISED_HAND = n(b'\xE2\x9C\x8B')
    VICTORY_HAND = n(b'\xE2\x9C\x8C')
    PENCIL = n(b'\xE2\x9C\x8F')
    BLACK_NIB = n(b'\xE2\x9C\x92')
    HEAVY_CHECK_MARK = n(b'\xE2\x9C\x94')
    HEAVY_MULTIPLICATION_X = n(b'\xE2\x9C\x96')
    SPARKLES = n(b'\xE2\x9C\xA8')
    EIGHT_SPOKED_ASTERISK = n(b'\xE2\x9C\xB3')
    EIGHT_POINTED_BLACK_STAR = n(b'\xE2\x9C\xB4')
    SNOWFLAKE = n(b'\xE2\x9D\x84')
    SPARKLE = n(b'\xE2\x9D\x87')
    CROSS_MARK = n(b'\xE2\x9D\x8C')
    NEGATIVE_SQUARED_CROSS_MARK = n(b'\xE2\x9D\x8E')
    BLACK_QUESTION_MARK_ORNAMENT = n(b'\xE2\x9D\x93')
    WHITE_QUESTION_MARK_ORNAMENT = n(b'\xE2\x9D\x94')
    WHITE_EXCLAMATION_MARK_ORNAMENT = n(b'\xE2\x9D\x95')
    HEAVY_EXCLAMATION_MARK_SYMBOL = n(b'\xE2\x9D\x97')
    HEAVY_BLACK_HEART = n(b'\xE2\x9D\xA4')
    HEAVY_PLUS_SIGN = n(b'\xE2\x9E\x95')
    HEAVY_MINUS_SIGN = n(b'\xE2\x9E\x96')
    HEAVY_DIVISION_SIGN = n(b'\xE2\x9E\x97')
    BLACK_RIGHTWARDS_ARROW = n(b'\xE2\x9E\xA1')
    CURLY_LOOP = n(b'\xE2\x9E\xB0')
    ROCKET = n(b'\xF0\x9F\x9A\x80')
    RAILWAY_CAR = n(b'\xF0\x9F\x9A\x83')
    HIGH_SPEED_TRAIN = n(b'\xF0\x9F\x9A\x84')
    HIGH_SPEED_TRAIN_WITH_BULLET_NOSE = n(b'\xF0\x9F\x9A\x85')
    METRO = n(b'\xF0\x9F\x9A\x87')
    STATION = n(b'\xF0\x9F\x9A\x89')
    BUS = n(b'\xF0\x9F\x9A\x8C')
    BUS_STOP = n(b'\xF0\x9F\x9A\x8F')
    AMBULANCE = n(b'\xF0\x9F\x9A\x91')
    FIRE_ENGINE = n(b'\xF0\x9F\x9A\x92')
    POLICE_CAR = n(b'\xF0\x9F\x9A\x93')
    TAXI = n(b'\xF0\x9F\x9A\x95')
    AUTOMOBILE = n(b'\xF0\x9F\x9A\x97')
    RECREATIONAL_VEHICLE = n(b'\xF0\x9F\x9A\x99')
    DELIVERY_TRUCK = n(b'\xF0\x9F\x9A\x9A')
    SHIP = n(b'\xF0\x9F\x9A\xA2')
    SPEEDBOAT = n(b'\xF0\x9F\x9A\xA4')
    HORIZONTAL_TRAFFIC_LIGHT = n(b'\xF0\x9F\x9A\xA5')
    CONSTRUCTION_SIGN = n(b'\xF0\x9F\x9A\xA7')
    POLICE_CARS_REVOLVING_LIGHT = n(b'\xF0\x9F\x9A\xA8')
    TRIANGULAR_FLAG_ON_POST = n(b'\xF0\x9F\x9A\xA9')
    DOOR = n(b'\xF0\x9F\x9A\xAA')
    NO_ENTRY_SIGN = n(b'\xF0\x9F\x9A\xAB')
    SMOKING_SYMBOL = n(b'\xF0\x9F\x9A\xAC')
    NO_SMOKING_SYMBOL = n(b'\xF0\x9F\x9A\xAD')
    BICYCLE = n(b'\xF0\x9F\x9A\xB2')
    PEDESTRIAN = n(b'\xF0\x9F\x9A\xB6')
    MENS_SYMBOL = n(b'\xF0\x9F\x9A\xB9')
    WOMENS_SYMBOL = n(b'\xF0\x9F\x9A\xBA')
    RESTROOM = n(b'\xF0\x9F\x9A\xBB')
    BABY_SYMBOL = n(b'\xF0\x9F\x9A\xBC')
    TOILET = n(b'\xF0\x9F\x9A\xBD')
    WATER_CLOSET = n(b'\xF0\x9F\x9A\xBE')
    BATH = n(b'\xF0\x9F\x9B\x80')
    CIRCLED_LATIN_CAPITAL_LETTER_M = n(b'\xE2\x93\x82')
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_A = n(b'\xF0\x9F\x85\xB0')
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_B = n(b'\xF0\x9F\x85\xB1')
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_O = n(b'\xF0\x9F\x85\xBE')
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_P = n(b'\xF0\x9F\x85\xBF')
    NEGATIVE_SQUARED_AB = n(b'\xF0\x9F\x86\x8E')
    SQUARED_CL = n(b'\xF0\x9F\x86\x91')
    SQUARED_COOL = n(b'\xF0\x9F\x86\x92')
    SQUARED_FREE = n(b'\xF0\x9F\x86\x93')
    SQUARED_ID = n(b'\xF0\x9F\x86\x94')
    SQUARED_NEW = n(b'\xF0\x9F\x86\x95')
    SQUARED_NG = n(b'\xF0\x9F\x86\x96')
    SQUARED_OK = n(b'\xF0\x9F\x86\x97')
    SQUARED_SOS = n(b'\xF0\x9F\x86\x98')
    SQUARED_UP_WITH_EXCLAMATION_MARK = n(b'\xF0\x9F\x86\x99')
    SQUARED_VS = n(b'\xF0\x9F\x86\x9A')
    REGIONAL_INDICATOR_SYMBOL_LETTER_D_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_E \
        = n(b'\xF0\x9F\x87\xA9\xF0\x9F\x87\xAA')
    REGIONAL_INDICATOR_SYMBOL_LETTER_G_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_B \
        = n(b'\xF0\x9F\x87\xAC\xF0\x9F\x87\xA7')
    REGIONAL_INDICATOR_SYMBOL_LETTER_C_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_N \
        = n(b'\xF0\x9F\x87\xA8\xF0\x9F\x87\xB3')
    REGIONAL_INDICATOR_SYMBOL_LETTER_J_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_P \
        = n(b'\xF0\x9F\x87\xAF\xF0\x9F\x87\xB5')
    REGIONAL_INDICATOR_SYMBOL_LETTER_K_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_R \
        = n(b'\xF0\x9F\x87\xB0\xF0\x9F\x87\xB7')
    REGIONAL_INDICATOR_SYMBOL_LETTER_F_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_R \
        = n(b'\xF0\x9F\x87\xAB\xF0\x9F\x87\xB7')
    REGIONAL_INDICATOR_SYMBOL_LETTER_E_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_S \
        = n(b'\xF0\x9F\x87\xAA\xF0\x9F\x87\xB8')
    REGIONAL_INDICATOR_SYMBOL_LETTER_I_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_T \
        = n(b'\xF0\x9F\x87\xAE\xF0\x9F\x87\xB9')
    REGIONAL_INDICATOR_SYMBOL_LETTER_U_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_S \
        = n(b'\xF0\x9F\x87\xBA\xF0\x9F\x87\xB8')
    REGIONAL_INDICATOR_SYMBOL_LETTER_R_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_U \
        = n(b'\xF0\x9F\x87\xB7\xF0\x9F\x87\xBA')
    SQUARED_KATAKANA_KOKO = n(b'\xF0\x9F\x88\x81')
    SQUARED_KATAKANA_SA = n(b'\xF0\x9F\x88\x82')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7121 = n(b'\xF0\x9F\x88\x9A')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6307 = n(b'\xF0\x9F\x88\xAF')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7981 = n(b'\xF0\x9F\x88\xB2')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7A7A = n(b'\xF0\x9F\x88\xB3')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_5408 = n(b'\xF0\x9F\x88\xB4')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6E80 = n(b'\xF0\x9F\x88\xB5')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6709 = n(b'\xF0\x9F\x88\xB6')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6708 = n(b'\xF0\x9F\x88\xB7')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7533 = n(b'\xF0\x9F\x88\xB8')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_5272 = n(b'\xF0\x9F\x88\xB9')
    SQUARED_CJK_UNIFIED_IDEOGRAPH_55B6 = n(b'\xF0\x9F\x88\xBA')
    CIRCLED_IDEOGRAPH_ADVANTAGE = n(b'\xF0\x9F\x89\x90')
    CIRCLED_IDEOGRAPH_ACCEPT = n(b'\xF0\x9F\x89\x91')
    COPYRIGHT_SIGN = n(b'\xC2\xA9')
    REGISTERED_SIGN = n(b'\xC2\xAE')
    DOUBLE_EXCLAMATION_MARK = n(b'\xE2\x80\xBC')
    EXCLAMATION_QUESTION_MARK = n(b'\xE2\x81\x89')
    DIGIT_EIGHT_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x38\xE2\x83\xA3')
    DIGIT_NINE_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x39\xE2\x83\xA3')
    DIGIT_SEVEN_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x37\xE2\x83\xA3')
    DIGIT_SIX_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x36\xE2\x83\xA3')
    DIGIT_ONE_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x31\xE2\x83\xA3')
    DIGIT_ZERO_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x30\xE2\x83\xA3')
    DIGIT_TWO_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x32\xE2\x83\xA3')
    DIGIT_THREE_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x33\xE2\x83\xA3')
    DIGIT_FIVE_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x35\xE2\x83\xA3')
    DIGIT_FOUR_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x34\xE2\x83\xA3')
    NUMBER_SIGN_PLUS_COMBINING_ENCLOSING_KEYCAP = n(b'\x23\xE2\x83\xA3')
    TRADE_MARK_SIGN = n(b'\xE2\x84\xA2')
    INFORMATION_SOURCE = n(b'\xE2\x84\xB9')
    LEFT_RIGHT_ARROW = n(b'\xE2\x86\x94')
    UP_DOWN_ARROW = n(b'\xE2\x86\x95')
    NORTH_WEST_ARROW = n(b'\xE2\x86\x96')
    NORTH_EAST_ARROW = n(b'\xE2\x86\x97')
    SOUTH_EAST_ARROW = n(b'\xE2\x86\x98')
    SOUTH_WEST_ARROW = n(b'\xE2\x86\x99')
    LEFTWARDS_ARROW_WITH_HOOK = n(b'\xE2\x86\xA9')
    RIGHTWARDS_ARROW_WITH_HOOK = n(b'\xE2\x86\xAA')
    WATCH = n(b'\xE2\x8C\x9A')
    HOURGLASS = n(b'\xE2\x8C\x9B')
    BLACK_RIGHT_POINTING_DOUBLE_TRIANGLE = n(b'\xE2\x8F\xA9')
    BLACK_LEFT_POINTING_DOUBLE_TRIANGLE = n(b'\xE2\x8F\xAA')
    BLACK_UP_POINTING_DOUBLE_TRIANGLE = n(b'\xE2\x8F\xAB')
    BLACK_DOWN_POINTING_DOUBLE_TRIANGLE = n(b'\xE2\x8F\xAC')
    ALARM_CLOCK = n(b'\xE2\x8F\xB0')
    HOURGLASS_WITH_FLOWING_SAND = n(b'\xE2\x8F\xB3')
    BLACK_SMALL_SQUARE = n(b'\xE2\x96\xAA')
    WHITE_SMALL_SQUARE = n(b'\xE2\x96\xAB')
    BLACK_RIGHT_POINTING_TRIANGLE = n(b'\xE2\x96\xB6')
    BLACK_LEFT_POINTING_TRIANGLE = n(b'\xE2\x97\x80')
    WHITE_MEDIUM_SQUARE = n(b'\xE2\x97\xBB')
    BLACK_MEDIUM_SQUARE = n(b'\xE2\x97\xBC')
    WHITE_MEDIUM_SMALL_SQUARE = n(b'\xE2\x97\xBD')
    BLACK_MEDIUM_SMALL_SQUARE = n(b'\xE2\x97\xBE')
    BLACK_SUN_WITH_RAYS = n(b'\xE2\x98\x80')
    CLOUD = n(b'\xE2\x98\x81')
    BLACK_TELEPHONE = n(b'\xE2\x98\x8E')
    BALLOT_BOX_WITH_CHECK = n(b'\xE2\x98\x91')
    UMBRELLA_WITH_RAIN_DROPS = n(b'\xE2\x98\x94')
    HOT_BEVERAGE = n(b'\xE2\x98\x95')
    WHITE_UP_POINTING_INDEX = n(b'\xE2\x98\x9D')
    WHITE_SMILING_FACE = n(b'\xE2\x98\xBA')
    ARIES = n(b'\xE2\x99\x88')
    TAURUS = n(b'\xE2\x99\x89')
    GEMINI = n(b'\xE2\x99\x8A')
    CANCER = n(b'\xE2\x99\x8B')
    LEO = n(b'\xE2\x99\x8C')
    VIRGO = n(b'\xE2\x99\x8D')
    LIBRA = n(b'\xE2\x99\x8E')
    SCORPIUS = n(b'\xE2\x99\x8F')
    SAGITTARIUS = n(b'\xE2\x99\x90')
    CAPRICORN = n(b'\xE2\x99\x91')
    AQUARIUS = n(b'\xE2\x99\x92')
    PISCES = n(b'\xE2\x99\x93')
    BLACK_SPADE_SUIT = n(b'\xE2\x99\xA0')
    BLACK_CLUB_SUIT = n(b'\xE2\x99\xA3')
    BLACK_HEART_SUIT = n(b'\xE2\x99\xA5')
    BLACK_DIAMOND_SUIT = n(b'\xE2\x99\xA6')
    HOT_SPRINGS = n(b'\xE2\x99\xA8')
    BLACK_UNIVERSAL_RECYCLING_SYMBOL = n(b'\xE2\x99\xBB')
    WHEELCHAIR_SYMBOL = n(b'\xE2\x99\xBF')
    ANCHOR = n(b'\xE2\x9A\x93')
    WARNING_SIGN = n(b'\xE2\x9A\xA0')
    HIGH_VOLTAGE_SIGN = n(b'\xE2\x9A\xA1')
    MEDIUM_WHITE_CIRCLE = n(b'\xE2\x9A\xAA')
    MEDIUM_BLACK_CIRCLE = n(b'\xE2\x9A\xAB')
    SOCCER_BALL = n(b'\xE2\x9A\xBD')
    BASEBALL = n(b'\xE2\x9A\xBE')
    SNOWMAN_WITHOUT_SNOW = n(b'\xE2\x9B\x84')
    SUN_BEHIND_CLOUD = n(b'\xE2\x9B\x85')
    OPHIUCHUS = n(b'\xE2\x9B\x8E')
    NO_ENTRY = n(b'\xE2\x9B\x94')
    CHURCH = n(b'\xE2\x9B\xAA')
    FOUNTAIN = n(b'\xE2\x9B\xB2')
    FLAG_IN_HOLE = n(b'\xE2\x9B\xB3')
    SAILBOAT = n(b'\xE2\x9B\xB5')
    TENT = n(b'\xE2\x9B\xBA')
    FUEL_PUMP = n(b'\xE2\x9B\xBD')
    ARROW_POINTING_RIGHTWARDS_THEN_CURVING_UPWARDS = n(b'\xE2\xA4\xB4')
    ARROW_POINTING_RIGHTWARDS_THEN_CURVING_DOWNWARDS = n(b'\xE2\xA4\xB5')
    LEFTWARDS_BLACK_ARROW = n(b'\xE2\xAC\x85')
    UPWARDS_BLACK_ARROW = n(b'\xE2\xAC\x86')
    DOWNWARDS_BLACK_ARROW = n(b'\xE2\xAC\x87')
    BLACK_LARGE_SQUARE = n(b'\xE2\xAC\x9B')
    WHITE_LARGE_SQUARE = n(b'\xE2\xAC\x9C')
    WHITE_MEDIUM_STAR = n(b'\xE2\xAD\x90')
    HEAVY_LARGE_CIRCLE = n(b'\xE2\xAD\x95')
    WAVY_DASH = n(b'\xE3\x80\xB0')
    PART_ALTERNATION_MARK = n(b'\xE3\x80\xBD')
    CIRCLED_IDEOGRAPH_CONGRATULATION = n(b'\xE3\x8A\x97')
    CIRCLED_IDEOGRAPH_SECRET = n(b'\xE3\x8A\x99')
    MAHJONG_TILE_RED_DRAGON = n(b'\xF0\x9F\x80\x84')
    PLAYING_CARD_BLACK_JOKER = n(b'\xF0\x9F\x83\x8F')
    CYCLONE = n(b'\xF0\x9F\x8C\x80')
    FOGGY = n(b'\xF0\x9F\x8C\x81')
    CLOSED_UMBRELLA = n(b'\xF0\x9F\x8C\x82')
    NIGHT_WITH_STARS = n(b'\xF0\x9F\x8C\x83')
    SUNRISE_OVER_MOUNTAINS = n(b'\xF0\x9F\x8C\x84')
    SUNRISE = n(b'\xF0\x9F\x8C\x85')
    CITYSCAPE_AT_DUSK = n(b'\xF0\x9F\x8C\x86')
    SUNSET_OVER_BUILDINGS = n(b'\xF0\x9F\x8C\x87')
    RAINBOW = n(b'\xF0\x9F\x8C\x88')
    BRIDGE_AT_NIGHT = n(b'\xF0\x9F\x8C\x89')
    WATER_WAVE = n(b'\xF0\x9F\x8C\x8A')
    VOLCANO = n(b'\xF0\x9F\x8C\x8B')
    MILKY_WAY = n(b'\xF0\x9F\x8C\x8C')
    EARTH_GLOBE_ASIA_AUSTRALIA = n(b'\xF0\x9F\x8C\x8F')
    NEW_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x91')
    FIRST_QUARTER_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x93')
    WAXING_GIBBOUS_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x94')
    FULL_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x95')
    CRESCENT_MOON = n(b'\xF0\x9F\x8C\x99')
    FIRST_QUARTER_MOON_WITH_FACE = n(b'\xF0\x9F\x8C\x9B')
    GLOWING_STAR = n(b'\xF0\x9F\x8C\x9F')
    SHOOTING_STAR = n(b'\xF0\x9F\x8C\xA0')
    CHESTNUT = n(b'\xF0\x9F\x8C\xB0')
    SEEDLING = n(b'\xF0\x9F\x8C\xB1')
    PALM_TREE = n(b'\xF0\x9F\x8C\xB4')
    CACTUS = n(b'\xF0\x9F\x8C\xB5')
    TULIP = n(b'\xF0\x9F\x8C\xB7')
    CHERRY_BLOSSOM = n(b'\xF0\x9F\x8C\xB8')
    ROSE = n(b'\xF0\x9F\x8C\xB9')
    HIBISCUS = n(b'\xF0\x9F\x8C\xBA')
    SUNFLOWER = n(b'\xF0\x9F\x8C\xBB')
    BLOSSOM = n(b'\xF0\x9F\x8C\xBC')
    EAR_OF_MAIZE = n(b'\xF0\x9F\x8C\xBD')
    EAR_OF_RICE = n(b'\xF0\x9F\x8C\xBE')
    HERB = n(b'\xF0\x9F\x8C\xBF')
    FOUR_LEAF_CLOVER = n(b'\xF0\x9F\x8D\x80')
    MAPLE_LEAF = n(b'\xF0\x9F\x8D\x81')
    FALLEN_LEAF = n(b'\xF0\x9F\x8D\x82')
    LEAF_FLUTTERING_IN_WIND = n(b'\xF0\x9F\x8D\x83')
    MUSHROOM = n(b'\xF0\x9F\x8D\x84')
    TOMATO = n(b'\xF0\x9F\x8D\x85')
    AUBERGINE = n(b'\xF0\x9F\x8D\x86')
    GRAPES = n(b'\xF0\x9F\x8D\x87')
    MELON = n(b'\xF0\x9F\x8D\x88')
    WATERMELON = n(b'\xF0\x9F\x8D\x89')
    TANGERINE = n(b'\xF0\x9F\x8D\x8A')
    BANANA = n(b'\xF0\x9F\x8D\x8C')
    PINEAPPLE = n(b'\xF0\x9F\x8D\x8D')
    RED_APPLE = n(b'\xF0\x9F\x8D\x8E')
    GREEN_APPLE = n(b'\xF0\x9F\x8D\x8F')
    PEACH = n(b'\xF0\x9F\x8D\x91')
    CHERRIES = n(b'\xF0\x9F\x8D\x92')
    STRAWBERRY = n(b'\xF0\x9F\x8D\x93')
    HAMBURGER = n(b'\xF0\x9F\x8D\x94')
    SLICE_OF_PIZZA = n(b'\xF0\x9F\x8D\x95')
    MEAT_ON_BONE = n(b'\xF0\x9F\x8D\x96')
    POULTRY_LEG = n(b'\xF0\x9F\x8D\x97')
    RICE_CRACKER = n(b'\xF0\x9F\x8D\x98')
    RICE_BALL = n(b'\xF0\x9F\x8D\x99')
    COOKED_RICE = n(b'\xF0\x9F\x8D\x9A')
    CURRY_AND_RICE = n(b'\xF0\x9F\x8D\x9B')
    STEAMING_BOWL = n(b'\xF0\x9F\x8D\x9C')
    SPAGHETTI = n(b'\xF0\x9F\x8D\x9D')
    BREAD = n(b'\xF0\x9F\x8D\x9E')
    FRENCH_FRIES = n(b'\xF0\x9F\x8D\x9F')
    ROASTED_SWEET_POTATO = n(b'\xF0\x9F\x8D\xA0')
    DANGO = n(b'\xF0\x9F\x8D\xA1')
    ODEN = n(b'\xF0\x9F\x8D\xA2')
    SUSHI = n(b'\xF0\x9F\x8D\xA3')
    FRIED_SHRIMP = n(b'\xF0\x9F\x8D\xA4')
    FISH_CAKE_WITH_SWIRL_DESIGN = n(b'\xF0\x9F\x8D\xA5')
    SOFT_ICE_CREAM = n(b'\xF0\x9F\x8D\xA6')
    SHAVED_ICE = n(b'\xF0\x9F\x8D\xA7')
    ICE_CREAM = n(b'\xF0\x9F\x8D\xA8')
    DOUGHNUT = n(b'\xF0\x9F\x8D\xA9')
    COOKIE = n(b'\xF0\x9F\x8D\xAA')
    CHOCOLATE_BAR = n(b'\xF0\x9F\x8D\xAB')
    CANDY = n(b'\xF0\x9F\x8D\xAC')
    LOLLIPOP = n(b'\xF0\x9F\x8D\xAD')
    CUSTARD = n(b'\xF0\x9F\x8D\xAE')
    HONEY_POT = n(b'\xF0\x9F\x8D\xAF')
    SHORTCAKE = n(b'\xF0\x9F\x8D\xB0')
    BENTO_BOX = n(b'\xF0\x9F\x8D\xB1')
    POT_OF_FOOD = n(b'\xF0\x9F\x8D\xB2')
    COOKING = n(b'\xF0\x9F\x8D\xB3')
    FORK_AND_KNIFE = n(b'\xF0\x9F\x8D\xB4')
    TEACUP_WITHOUT_HANDLE = n(b'\xF0\x9F\x8D\xB5')
    SAKE_BOTTLE_AND_CUP = n(b'\xF0\x9F\x8D\xB6')
    WINE_GLASS = n(b'\xF0\x9F\x8D\xB7')
    COCKTAIL_GLASS = n(b'\xF0\x9F\x8D\xB8')
    TROPICAL_DRINK = n(b'\xF0\x9F\x8D\xB9')
    BEER_MUG = n(b'\xF0\x9F\x8D\xBA')
    CLINKING_BEER_MUGS = n(b'\xF0\x9F\x8D\xBB')
    RIBBON = n(b'\xF0\x9F\x8E\x80')
    WRAPPED_PRESENT = n(b'\xF0\x9F\x8E\x81')
    BIRTHDAY_CAKE = n(b'\xF0\x9F\x8E\x82')
    JACK_O_LANTERN = n(b'\xF0\x9F\x8E\x83')
    CHRISTMAS_TREE = n(b'\xF0\x9F\x8E\x84')
    FATHER_CHRISTMAS = n(b'\xF0\x9F\x8E\x85')
    FIREWORKS = n(b'\xF0\x9F\x8E\x86')
    FIREWORK_SPARKLER = n(b'\xF0\x9F\x8E\x87')
    BALLOON = n(b'\xF0\x9F\x8E\x88')
    PARTY_POPPER = n(b'\xF0\x9F\x8E\x89')
    CONFETTI_BALL = n(b'\xF0\x9F\x8E\x8A')
    TANABATA_TREE = n(b'\xF0\x9F\x8E\x8B')
    CROSSED_FLAGS = n(b'\xF0\x9F\x8E\x8C')
    PINE_DECORATION = n(b'\xF0\x9F\x8E\x8D')
    JAPANESE_DOLLS = n(b'\xF0\x9F\x8E\x8E')
    CARP_STREAMER = n(b'\xF0\x9F\x8E\x8F')
    WIND_CHIME = n(b'\xF0\x9F\x8E\x90')
    MOON_VIEWING_CEREMONY = n(b'\xF0\x9F\x8E\x91')
    SCHOOL_SATCHEL = n(b'\xF0\x9F\x8E\x92')
    GRADUATION_CAP = n(b'\xF0\x9F\x8E\x93')
    CAROUSEL_HORSE = n(b'\xF0\x9F\x8E\xA0')
    FERRIS_WHEEL = n(b'\xF0\x9F\x8E\xA1')
    ROLLER_COASTER = n(b'\xF0\x9F\x8E\xA2')
    FISHING_POLE_AND_FISH = n(b'\xF0\x9F\x8E\xA3')
    MICROPHONE = n(b'\xF0\x9F\x8E\xA4')
    MOVIE_CAMERA = n(b'\xF0\x9F\x8E\xA5')
    CINEMA = n(b'\xF0\x9F\x8E\xA6')
    HEADPHONE = n(b'\xF0\x9F\x8E\xA7')
    ARTIST_PALETTE = n(b'\xF0\x9F\x8E\xA8')
    TOP_HAT = n(b'\xF0\x9F\x8E\xA9')
    CIRCUS_TENT = n(b'\xF0\x9F\x8E\xAA')
    TICKET = n(b'\xF0\x9F\x8E\xAB')
    CLAPPER_BOARD = n(b'\xF0\x9F\x8E\xAC')
    PERFORMING_ARTS = n(b'\xF0\x9F\x8E\xAD')
    VIDEO_GAME = n(b'\xF0\x9F\x8E\xAE')
    DIRECT_HIT = n(b'\xF0\x9F\x8E\xAF')
    SLOT_MACHINE = n(b'\xF0\x9F\x8E\xB0')
    BILLIARDS = n(b'\xF0\x9F\x8E\xB1')
    GAME_DIE = n(b'\xF0\x9F\x8E\xB2')
    BOWLING = n(b'\xF0\x9F\x8E\xB3')
    FLOWER_PLAYING_CARDS = n(b'\xF0\x9F\x8E\xB4')
    MUSICAL_NOTE = n(b'\xF0\x9F\x8E\xB5')
    MULTIPLE_MUSICAL_NOTES = n(b'\xF0\x9F\x8E\xB6')
    SAXOPHONE = n(b'\xF0\x9F\x8E\xB7')
    GUITAR = n(b'\xF0\x9F\x8E\xB8')
    MUSICAL_KEYBOARD = n(b'\xF0\x9F\x8E\xB9')
    TRUMPET = n(b'\xF0\x9F\x8E\xBA')
    VIOLIN = n(b'\xF0\x9F\x8E\xBB')
    MUSICAL_SCORE = n(b'\xF0\x9F\x8E\xBC')
    RUNNING_SHIRT_WITH_SASH = n(b'\xF0\x9F\x8E\xBD')
    TENNIS_RACQUET_AND_BALL = n(b'\xF0\x9F\x8E\xBE')
    SKI_AND_SKI_BOOT = n(b'\xF0\x9F\x8E\xBF')
    BASKETBALL_AND_HOOP = n(b'\xF0\x9F\x8F\x80')
    CHEQUERED_FLAG = n(b'\xF0\x9F\x8F\x81')
    SNOWBOARDER = n(b'\xF0\x9F\x8F\x82')
    RUNNER = n(b'\xF0\x9F\x8F\x83')
    SURFER = n(b'\xF0\x9F\x8F\x84')
    TROPHY = n(b'\xF0\x9F\x8F\x86')
    AMERICAN_FOOTBALL = n(b'\xF0\x9F\x8F\x88')
    SWIMMER = n(b'\xF0\x9F\x8F\x8A')
    HOUSE_BUILDING = n(b'\xF0\x9F\x8F\xA0')
    HOUSE_WITH_GARDEN = n(b'\xF0\x9F\x8F\xA1')
    OFFICE_BUILDING = n(b'\xF0\x9F\x8F\xA2')
    JAPANESE_POST_OFFICE = n(b'\xF0\x9F\x8F\xA3')
    HOSPITAL = n(b'\xF0\x9F\x8F\xA5')
    BANK = n(b'\xF0\x9F\x8F\xA6')
    AUTOMATED_TELLER_MACHINE = n(b'\xF0\x9F\x8F\xA7')
    HOTEL = n(b'\xF0\x9F\x8F\xA8')
    LOVE_HOTEL = n(b'\xF0\x9F\x8F\xA9')
    CONVENIENCE_STORE = n(b'\xF0\x9F\x8F\xAA')
    SCHOOL = n(b'\xF0\x9F\x8F\xAB')
    DEPARTMENT_STORE = n(b'\xF0\x9F\x8F\xAC')
    FACTORY = n(b'\xF0\x9F\x8F\xAD')
    IZAKAYA_LANTERN = n(b'\xF0\x9F\x8F\xAE')
    JAPANESE_CASTLE = n(b'\xF0\x9F\x8F\xAF')
    EUROPEAN_CASTLE = n(b'\xF0\x9F\x8F\xB0')
    SNAIL = n(b'\xF0\x9F\x90\x8C')
    SNAKE = n(b'\xF0\x9F\x90\x8D')
    HORSE = n(b'\xF0\x9F\x90\x8E')
    SHEEP = n(b'\xF0\x9F\x90\x91')
    MONKEY = n(b'\xF0\x9F\x90\x92')
    CHICKEN = n(b'\xF0\x9F\x90\x94')
    BOAR = n(b'\xF0\x9F\x90\x97')
    ELEPHANT = n(b'\xF0\x9F\x90\x98')
    OCTOPUS = n(b'\xF0\x9F\x90\x99')
    SPIRAL_SHELL = n(b'\xF0\x9F\x90\x9A')
    BUG = n(b'\xF0\x9F\x90\x9B')
    ANT = n(b'\xF0\x9F\x90\x9C')
    HONEYBEE = n(b'\xF0\x9F\x90\x9D')
    LADY_BEETLE = n(b'\xF0\x9F\x90\x9E')
    FISH = n(b'\xF0\x9F\x90\x9F')
    TROPICAL_FISH = n(b'\xF0\x9F\x90\xA0')
    BLOWFISH = n(b'\xF0\x9F\x90\xA1')
    TURTLE = n(b'\xF0\x9F\x90\xA2')
    HATCHING_CHICK = n(b'\xF0\x9F\x90\xA3')
    BABY_CHICK = n(b'\xF0\x9F\x90\xA4')
    FRONT_FACING_BABY_CHICK = n(b'\xF0\x9F\x90\xA5')
    BIRD = n(b'\xF0\x9F\x90\xA6')
    PENGUIN = n(b'\xF0\x9F\x90\xA7')
    KOALA = n(b'\xF0\x9F\x90\xA8')
    POODLE = n(b'\xF0\x9F\x90\xA9')
    BACTRIAN_CAMEL = n(b'\xF0\x9F\x90\xAB')
    DOLPHIN = n(b'\xF0\x9F\x90\xAC')
    MOUSE_FACE = n(b'\xF0\x9F\x90\xAD')
    COW_FACE = n(b'\xF0\x9F\x90\xAE')
    TIGER_FACE = n(b'\xF0\x9F\x90\xAF')
    RABBIT_FACE = n(b'\xF0\x9F\x90\xB0')
    CAT_FACE = n(b'\xF0\x9F\x90\xB1')
    DRAGON_FACE = n(b'\xF0\x9F\x90\xB2')
    SPOUTING_WHALE = n(b'\xF0\x9F\x90\xB3')
    HORSE_FACE = n(b'\xF0\x9F\x90\xB4')
    MONKEY_FACE = n(b'\xF0\x9F\x90\xB5')
    DOG_FACE = n(b'\xF0\x9F\x90\xB6')
    PIG_FACE = n(b'\xF0\x9F\x90\xB7')
    FROG_FACE = n(b'\xF0\x9F\x90\xB8')
    HAMSTER_FACE = n(b'\xF0\x9F\x90\xB9')
    WOLF_FACE = n(b'\xF0\x9F\x90\xBA')
    BEAR_FACE = n(b'\xF0\x9F\x90\xBB')
    PANDA_FACE = n(b'\xF0\x9F\x90\xBC')
    PIG_NOSE = n(b'\xF0\x9F\x90\xBD')
    PAW_PRINTS = n(b'\xF0\x9F\x90\xBE')
    EYES = n(b'\xF0\x9F\x91\x80')
    EAR = n(b'\xF0\x9F\x91\x82')
    NOSE = n(b'\xF0\x9F\x91\x83')
    MOUTH = n(b'\xF0\x9F\x91\x84')
    TONGUE = n(b'\xF0\x9F\x91\x85')
    WHITE_UP_POINTING_BACKHAND_INDEX = n(b'\xF0\x9F\x91\x86')
    WHITE_DOWN_POINTING_BACKHAND_INDEX = n(b'\xF0\x9F\x91\x87')
    WHITE_LEFT_POINTING_BACKHAND_INDEX = n(b'\xF0\x9F\x91\x88')
    WHITE_RIGHT_POINTING_BACKHAND_INDEX = n(b'\xF0\x9F\x91\x89')
    FISTED_HAND_SIGN = n(b'\xF0\x9F\x91\x8A')
    WAVING_HAND_SIGN = n(b'\xF0\x9F\x91\x8B')
    OK_HAND_SIGN = n(b'\xF0\x9F\x91\x8C')
    THUMBS_UP_SIGN = n(b'\xF0\x9F\x91\x8D')
    THUMBS_DOWN_SIGN = n(b'\xF0\x9F\x91\x8E')
    CLAPPING_HANDS_SIGN = n(b'\xF0\x9F\x91\x8F')
    OPEN_HANDS_SIGN = n(b'\xF0\x9F\x91\x90')
    CROWN = n(b'\xF0\x9F\x91\x91')
    WOMANS_HAT = n(b'\xF0\x9F\x91\x92')
    EYEGLASSES = n(b'\xF0\x9F\x91\x93')
    NECKTIE = n(b'\xF0\x9F\x91\x94')
    T_SHIRT = n(b'\xF0\x9F\x91\x95')
    JEANS = n(b'\xF0\x9F\x91\x96')
    DRESS = n(b'\xF0\x9F\x91\x97')
    KIMONO = n(b'\xF0\x9F\x91\x98')
    BIKINI = n(b'\xF0\x9F\x91\x99')
    WOMANS_CLOTHES = n(b'\xF0\x9F\x91\x9A')
    PURSE = n(b'\xF0\x9F\x91\x9B')
    HANDBAG = n(b'\xF0\x9F\x91\x9C')
    POUCH = n(b'\xF0\x9F\x91\x9D')
    MANS_SHOE = n(b'\xF0\x9F\x91\x9E')
    ATHLETIC_SHOE = n(b'\xF0\x9F\x91\x9F')
    HIGH_HEELED_SHOE = n(b'\xF0\x9F\x91\xA0')
    WOMANS_SANDAL = n(b'\xF0\x9F\x91\xA1')
    WOMANS_BOOTS = n(b'\xF0\x9F\x91\xA2')
    FOOTPRINTS = n(b'\xF0\x9F\x91\xA3')
    BUST_IN_SILHOUETTE = n(b'\xF0\x9F\x91\xA4')
    BOY = n(b'\xF0\x9F\x91\xA6')
    GIRL = n(b'\xF0\x9F\x91\xA7')
    MAN = n(b'\xF0\x9F\x91\xA8')
    WOMAN = n(b'\xF0\x9F\x91\xA9')
    FAMILY = n(b'\xF0\x9F\x91\xAA')
    MAN_AND_WOMAN_HOLDING_HANDS = n(b'\xF0\x9F\x91\xAB')
    POLICE_OFFICER = n(b'\xF0\x9F\x91\xAE')
    WOMAN_WITH_BUNNY_EARS = n(b'\xF0\x9F\x91\xAF')
    BRIDE_WITH_VEIL = n(b'\xF0\x9F\x91\xB0')
    PERSON_WITH_BLOND_HAIR = n(b'\xF0\x9F\x91\xB1')
    MAN_WITH_GUA_PI_MAO = n(b'\xF0\x9F\x91\xB2')
    MAN_WITH_TURBAN = n(b'\xF0\x9F\x91\xB3')
    OLDER_MAN = n(b'\xF0\x9F\x91\xB4')
    OLDER_WOMAN = n(b'\xF0\x9F\x91\xB5')
    BABY = n(b'\xF0\x9F\x91\xB6')
    CONSTRUCTION_WORKER = n(b'\xF0\x9F\x91\xB7')
    PRINCESS = n(b'\xF0\x9F\x91\xB8')
    JAPANESE_OGRE = n(b'\xF0\x9F\x91\xB9')
    JAPANESE_GOBLIN = n(b'\xF0\x9F\x91\xBA')
    GHOST = n(b'\xF0\x9F\x91\xBB')
    BABY_ANGEL = n(b'\xF0\x9F\x91\xBC')
    EXTRATERRESTRIAL_ALIEN = n(b'\xF0\x9F\x91\xBD')
    ALIEN_MONSTER = n(b'\xF0\x9F\x91\xBE')
    IMP = n(b'\xF0\x9F\x91\xBF')
    SKULL = n(b'\xF0\x9F\x92\x80')
    INFORMATION_DESK_PERSON = n(b'\xF0\x9F\x92\x81')
    GUARDSMAN = n(b'\xF0\x9F\x92\x82')
    DANCER = n(b'\xF0\x9F\x92\x83')
    LIPSTICK = n(b'\xF0\x9F\x92\x84')
    NAIL_POLISH = n(b'\xF0\x9F\x92\x85')
    FACE_MASSAGE = n(b'\xF0\x9F\x92\x86')
    HAIRCUT = n(b'\xF0\x9F\x92\x87')
    BARBER_POLE = n(b'\xF0\x9F\x92\x88')
    SYRINGE = n(b'\xF0\x9F\x92\x89')
    PILL = n(b'\xF0\x9F\x92\x8A')
    KISS_MARK = n(b'\xF0\x9F\x92\x8B')
    LOVE_LETTER = n(b'\xF0\x9F\x92\x8C')
    RING = n(b'\xF0\x9F\x92\x8D')
    GEM_STONE = n(b'\xF0\x9F\x92\x8E')
    KISS = n(b'\xF0\x9F\x92\x8F')
    BOUQUET = n(b'\xF0\x9F\x92\x90')
    COUPLE_WITH_HEART = n(b'\xF0\x9F\x92\x91')
    WEDDING = n(b'\xF0\x9F\x92\x92')
    BEATING_HEART = n(b'\xF0\x9F\x92\x93')
    BROKEN_HEART = n(b'\xF0\x9F\x92\x94')
    TWO_HEARTS = n(b'\xF0\x9F\x92\x95')
    SPARKLING_HEART = n(b'\xF0\x9F\x92\x96')
    GROWING_HEART = n(b'\xF0\x9F\x92\x97')
    HEART_WITH_ARROW = n(b'\xF0\x9F\x92\x98')
    BLUE_HEART = n(b'\xF0\x9F\x92\x99')
    GREEN_HEART = n(b'\xF0\x9F\x92\x9A')
    YELLOW_HEART = n(b'\xF0\x9F\x92\x9B')
    PURPLE_HEART = n(b'\xF0\x9F\x92\x9C')
    HEART_WITH_RIBBON = n(b'\xF0\x9F\x92\x9D')
    REVOLVING_HEARTS = n(b'\xF0\x9F\x92\x9E')
    HEART_DECORATION = n(b'\xF0\x9F\x92\x9F')
    DIAMOND_SHAPE_WITH_A_DOT_INSIDE = n(b'\xF0\x9F\x92\xA0')
    ELECTRIC_LIGHT_BULB = n(b'\xF0\x9F\x92\xA1')
    ANGER_SYMBOL = n(b'\xF0\x9F\x92\xA2')
    BOMB = n(b'\xF0\x9F\x92\xA3')
    SLEEPING_SYMBOL = n(b'\xF0\x9F\x92\xA4')
    COLLISION_SYMBOL = n(b'\xF0\x9F\x92\xA5')
    SPLASHING_SWEAT_SYMBOL = n(b'\xF0\x9F\x92\xA6')
    DROPLET = n(b'\xF0\x9F\x92\xA7')
    DASH_SYMBOL = n(b'\xF0\x9F\x92\xA8')
    PILE_OF_POO = n(b'\xF0\x9F\x92\xA9')
    FLEXED_BICEPS = n(b'\xF0\x9F\x92\xAA')
    DIZZY_SYMBOL = n(b'\xF0\x9F\x92\xAB')
    SPEECH_BALLOON = n(b'\xF0\x9F\x92\xAC')
    WHITE_FLOWER = n(b'\xF0\x9F\x92\xAE')
    HUNDRED_POINTS_SYMBOL = n(b'\xF0\x9F\x92\xAF')
    MONEY_BAG = n(b'\xF0\x9F\x92\xB0')
    CURRENCY_EXCHANGE = n(b'\xF0\x9F\x92\xB1')
    HEAVY_DOLLAR_SIGN = n(b'\xF0\x9F\x92\xB2')
    CREDIT_CARD = n(b'\xF0\x9F\x92\xB3')
    BANKNOTE_WITH_YEN_SIGN = n(b'\xF0\x9F\x92\xB4')
    BANKNOTE_WITH_DOLLAR_SIGN = n(b'\xF0\x9F\x92\xB5')
    MONEY_WITH_WINGS = n(b'\xF0\x9F\x92\xB8')
    CHART_WITH_UPWARDS_TREND_AND_YEN_SIGN = n(b'\xF0\x9F\x92\xB9')
    SEAT = n(b'\xF0\x9F\x92\xBA')
    PERSONAL_COMPUTER = n(b'\xF0\x9F\x92\xBB')
    BRIEFCASE = n(b'\xF0\x9F\x92\xBC')
    MINIDISC = n(b'\xF0\x9F\x92\xBD')
    FLOPPY_DISK = n(b'\xF0\x9F\x92\xBE')
    OPTICAL_DISC = n(b'\xF0\x9F\x92\xBF')
    DVD = n(b'\xF0\x9F\x93\x80')
    FILE_FOLDER = n(b'\xF0\x9F\x93\x81')
    OPEN_FILE_FOLDER = n(b'\xF0\x9F\x93\x82')
    PAGE_WITH_CURL = n(b'\xF0\x9F\x93\x83')
    PAGE_FACING_UP = n(b'\xF0\x9F\x93\x84')
    CALENDAR = n(b'\xF0\x9F\x93\x85')
    TEAR_OFF_CALENDAR = n(b'\xF0\x9F\x93\x86')
    CARD_INDEX = n(b'\xF0\x9F\x93\x87')
    CHART_WITH_UPWARDS_TREND = n(b'\xF0\x9F\x93\x88')
    CHART_WITH_DOWNWARDS_TREND = n(b'\xF0\x9F\x93\x89')
    BAR_CHART = n(b'\xF0\x9F\x93\x8A')
    CLIPBOARD = n(b'\xF0\x9F\x93\x8B')
    PUSHPIN = n(b'\xF0\x9F\x93\x8C')
    ROUND_PUSHPIN = n(b'\xF0\x9F\x93\x8D')
    PAPERCLIP = n(b'\xF0\x9F\x93\x8E')
    STRAIGHT_RULER = n(b'\xF0\x9F\x93\x8F')
    TRIANGULAR_RULER = n(b'\xF0\x9F\x93\x90')
    BOOKMARK_TABS = n(b'\xF0\x9F\x93\x91')
    LEDGER = n(b'\xF0\x9F\x93\x92')
    NOTEBOOK = n(b'\xF0\x9F\x93\x93')
    NOTEBOOK_WITH_DECORATIVE_COVER = n(b'\xF0\x9F\x93\x94')
    CLOSED_BOOK = n(b'\xF0\x9F\x93\x95')
    OPEN_BOOK = n(b'\xF0\x9F\x93\x96')
    GREEN_BOOK = n(b'\xF0\x9F\x93\x97')
    BLUE_BOOK = n(b'\xF0\x9F\x93\x98')
    ORANGE_BOOK = n(b'\xF0\x9F\x93\x99')
    BOOKS = n(b'\xF0\x9F\x93\x9A')
    NAME_BADGE = n(b'\xF0\x9F\x93\x9B')
    SCROLL = n(b'\xF0\x9F\x93\x9C')
    MEMO = n(b'\xF0\x9F\x93\x9D')
    TELEPHONE_RECEIVER = n(b'\xF0\x9F\x93\x9E')
    PAGER = n(b'\xF0\x9F\x93\x9F')
    FAX_MACHINE = n(b'\xF0\x9F\x93\xA0')
    SATELLITE_ANTENNA = n(b'\xF0\x9F\x93\xA1')
    PUBLIC_ADDRESS_LOUDSPEAKER = n(b'\xF0\x9F\x93\xA2')
    CHEERING_MEGAPHONE = n(b'\xF0\x9F\x93\xA3')
    OUTBOX_TRAY = n(b'\xF0\x9F\x93\xA4')
    INBOX_TRAY = n(b'\xF0\x9F\x93\xA5')
    PACKAGE = n(b'\xF0\x9F\x93\xA6')
    E_MAIL_SYMBOL = n(b'\xF0\x9F\x93\xA7')
    INCOMING_ENVELOPE = n(b'\xF0\x9F\x93\xA8')
    ENVELOPE_WITH_DOWNWARDS_ARROW_ABOVE = n(b'\xF0\x9F\x93\xA9')
    CLOSED_MAILBOX_WITH_LOWERED_FLAG = n(b'\xF0\x9F\x93\xAA')
    CLOSED_MAILBOX_WITH_RAISED_FLAG = n(b'\xF0\x9F\x93\xAB')
    POSTBOX = n(b'\xF0\x9F\x93\xAE')
    NEWSPAPER = n(b'\xF0\x9F\x93\xB0')
    MOBILE_PHONE = n(b'\xF0\x9F\x93\xB1')
    MOBILE_PHONE_WITH_RIGHTWARDS_ARROW_AT_LEFT = n(b'\xF0\x9F\x93\xB2')
    VIBRATION_MODE = n(b'\xF0\x9F\x93\xB3')
    MOBILE_PHONE_OFF = n(b'\xF0\x9F\x93\xB4')
    ANTENNA_WITH_BARS = n(b'\xF0\x9F\x93\xB6')
    CAMERA = n(b'\xF0\x9F\x93\xB7')
    VIDEO_CAMERA = n(b'\xF0\x9F\x93\xB9')
    TELEVISION = n(b'\xF0\x9F\x93\xBA')
    RADIO = n(b'\xF0\x9F\x93\xBB')
    VIDEOCASSETTE = n(b'\xF0\x9F\x93\xBC')
    CLOCKWISE_DOWNWARDS_AND_UPWARDS_OPEN_CIRCLE_ARROWS = n(b'\xF0\x9F\x94\x83')
    SPEAKER_WITH_THREE_SOUND_WAVES = n(b'\xF0\x9F\x94\x8A')
    BATTERY = n(b'\xF0\x9F\x94\x8B')
    ELECTRIC_PLUG = n(b'\xF0\x9F\x94\x8C')
    LEFT_POINTING_MAGNIFYING_GLASS = n(b'\xF0\x9F\x94\x8D')
    RIGHT_POINTING_MAGNIFYING_GLASS = n(b'\xF0\x9F\x94\x8E')
    LOCK_WITH_INK_PEN = n(b'\xF0\x9F\x94\x8F')
    CLOSED_LOCK_WITH_KEY = n(b'\xF0\x9F\x94\x90')
    KEY = n(b'\xF0\x9F\x94\x91')
    LOCK = n(b'\xF0\x9F\x94\x92')
    OPEN_LOCK = n(b'\xF0\x9F\x94\x93')
    BELL = n(b'\xF0\x9F\x94\x94')
    BOOKMARK = n(b'\xF0\x9F\x94\x96')
    LINK_SYMBOL = n(b'\xF0\x9F\x94\x97')
    RADIO_BUTTON = n(b'\xF0\x9F\x94\x98')
    BACK_WITH_LEFTWARDS_ARROW_ABOVE = n(b'\xF0\x9F\x94\x99')
    END_WITH_LEFTWARDS_ARROW_ABOVE = n(b'\xF0\x9F\x94\x9A')
    ON_WITH_EXCLAMATION_MARK_WITH_LEFT_RIGHT_ARROW_ABOVE = n(b'\xF0\x9F\x94\x9B')
    SOON_WITH_RIGHTWARDS_ARROW_ABOVE = n(b'\xF0\x9F\x94\x9C')
    TOP_WITH_UPWARDS_ARROW_ABOVE = n(b'\xF0\x9F\x94\x9D')
    NO_ONE_UNDER_EIGHTEEN_SYMBOL = n(b'\xF0\x9F\x94\x9E')
    KEYCAP_TEN = n(b'\xF0\x9F\x94\x9F')
    INPUT_SYMBOL_FOR_LATIN_CAPITAL_LETTERS = n(b'\xF0\x9F\x94\xA0')
    INPUT_SYMBOL_FOR_LATIN_SMALL_LETTERS = n(b'\xF0\x9F\x94\xA1')
    INPUT_SYMBOL_FOR_NUMBERS = n(b'\xF0\x9F\x94\xA2')
    INPUT_SYMBOL_FOR_SYMBOLS = n(b'\xF0\x9F\x94\xA3')
    INPUT_SYMBOL_FOR_LATIN_LETTERS = n(b'\xF0\x9F\x94\xA4')
    FIRE = n(b'\xF0\x9F\x94\xA5')
    ELECTRIC_TORCH = n(b'\xF0\x9F\x94\xA6')
    WRENCH = n(b'\xF0\x9F\x94\xA7')
    HAMMER = n(b'\xF0\x9F\x94\xA8')
    NUT_AND_BOLT = n(b'\xF0\x9F\x94\xA9')
    HOCHO = n(b'\xF0\x9F\x94\xAA')
    PISTOL = n(b'\xF0\x9F\x94\xAB')
    CRYSTAL_BALL = n(b'\xF0\x9F\x94\xAE')
    SIX_POINTED_STAR_WITH_MIDDLE_DOT = n(b'\xF0\x9F\x94\xAF')
    JAPANESE_SYMBOL_FOR_BEGINNER = n(b'\xF0\x9F\x94\xB0')
    TRIDENT_EMBLEM = n(b'\xF0\x9F\x94\xB1')
    BLACK_SQUARE_BUTTON = n(b'\xF0\x9F\x94\xB2')
    WHITE_SQUARE_BUTTON = n(b'\xF0\x9F\x94\xB3')
    LARGE_RED_CIRCLE = n(b'\xF0\x9F\x94\xB4')
    LARGE_BLUE_CIRCLE = n(b'\xF0\x9F\x94\xB5')
    LARGE_ORANGE_DIAMOND = n(b'\xF0\x9F\x94\xB6')
    LARGE_BLUE_DIAMOND = n(b'\xF0\x9F\x94\xB7')
    SMALL_ORANGE_DIAMOND = n(b'\xF0\x9F\x94\xB8')
    SMALL_BLUE_DIAMOND = n(b'\xF0\x9F\x94\xB9')
    UP_POINTING_RED_TRIANGLE = n(b'\xF0\x9F\x94\xBA')
    DOWN_POINTING_RED_TRIANGLE = n(b'\xF0\x9F\x94\xBB')
    UP_POINTING_SMALL_RED_TRIANGLE = n(b'\xF0\x9F\x94\xBC')
    DOWN_POINTING_SMALL_RED_TRIANGLE = n(b'\xF0\x9F\x94\xBD')
    CLOCK_FACE_ONE_OCLOCK = n(b'\xF0\x9F\x95\x90')
    CLOCK_FACE_TWO_OCLOCK = n(b'\xF0\x9F\x95\x91')
    CLOCK_FACE_THREE_OCLOCK = n(b'\xF0\x9F\x95\x92')
    CLOCK_FACE_FOUR_OCLOCK = n(b'\xF0\x9F\x95\x93')
    CLOCK_FACE_FIVE_OCLOCK = n(b'\xF0\x9F\x95\x94')
    CLOCK_FACE_SIX_OCLOCK = n(b'\xF0\x9F\x95\x95')
    CLOCK_FACE_SEVEN_OCLOCK = n(b'\xF0\x9F\x95\x96')
    CLOCK_FACE_EIGHT_OCLOCK = n(b'\xF0\x9F\x95\x97')
    CLOCK_FACE_NINE_OCLOCK = n(b'\xF0\x9F\x95\x98')
    CLOCK_FACE_TEN_OCLOCK = n(b'\xF0\x9F\x95\x99')
    CLOCK_FACE_ELEVEN_OCLOCK = n(b'\xF0\x9F\x95\x9A')
    CLOCK_FACE_TWELVE_OCLOCK = n(b'\xF0\x9F\x95\x9B')
    MOUNT_FUJI = n(b'\xF0\x9F\x97\xBB')
    TOKYO_TOWER = n(b'\xF0\x9F\x97\xBC')
    STATUE_OF_LIBERTY = n(b'\xF0\x9F\x97\xBD')
    SILHOUETTE_OF_JAPAN = n(b'\xF0\x9F\x97\xBE')
    MOYAI = n(b'\xF0\x9F\x97\xBF')
    GRINNING_FACE = n(b'\xF0\x9F\x98\x80')
    SMILING_FACE_WITH_HALO = n(b'\xF0\x9F\x98\x87')
    SMILING_FACE_WITH_HORNS = n(b'\xF0\x9F\x98\x88')
    SMILING_FACE_WITH_SUNGLASSES = n(b'\xF0\x9F\x98\x8E')
    NEUTRAL_FACE = n(b'\xF0\x9F\x98\x90')
    EXPRESSIONLESS_FACE = n(b'\xF0\x9F\x98\x91')
    CONFUSED_FACE = n(b'\xF0\x9F\x98\x95')
    KISSING_FACE = n(b'\xF0\x9F\x98\x97')
    KISSING_FACE_WITH_SMILING_EYES = n(b'\xF0\x9F\x98\x99')
    FACE_WITH_STUCK_OUT_TONGUE = n(b'\xF0\x9F\x98\x9B')
    WORRIED_FACE = n(b'\xF0\x9F\x98\x9F')
    FROWNING_FACE_WITH_OPEN_MOUTH = n(b'\xF0\x9F\x98\xA6')
    ANGUISHED_FACE = n(b'\xF0\x9F\x98\xA7')
    GRIMACING_FACE = n(b'\xF0\x9F\x98\xAC')
    FACE_WITH_OPEN_MOUTH = n(b'\xF0\x9F\x98\xAE')
    HUSHED_FACE = n(b'\xF0\x9F\x98\xAF')
    SLEEPING_FACE = n(b'\xF0\x9F\x98\xB4')
    FACE_WITHOUT_MOUTH = n(b'\xF0\x9F\x98\xB6')
    HELICOPTER = n(b'\xF0\x9F\x9A\x81')
    STEAM_LOCOMOTIVE = n(b'\xF0\x9F\x9A\x82')
    TRAIN = n(b'\xF0\x9F\x9A\x86')
    LIGHT_RAIL = n(b'\xF0\x9F\x9A\x88')
    TRAM = n(b'\xF0\x9F\x9A\x8A')
    ONCOMING_BUS = n(b'\xF0\x9F\x9A\x8D')
    TROLLEYBUS = n(b'\xF0\x9F\x9A\x8E')
    MINIBUS = n(b'\xF0\x9F\x9A\x90')
    ONCOMING_POLICE_CAR = n(b'\xF0\x9F\x9A\x94')
    ONCOMING_TAXI = n(b'\xF0\x9F\x9A\x96')
    ONCOMING_AUTOMOBILE = n(b'\xF0\x9F\x9A\x98')
    ARTICULATED_LORRY = n(b'\xF0\x9F\x9A\x9B')
    TRACTOR = n(b'\xF0\x9F\x9A\x9C')
    MONORAIL = n(b'\xF0\x9F\x9A\x9D')
    MOUNTAIN_RAILWAY = n(b'\xF0\x9F\x9A\x9E')
    SUSPENSION_RAILWAY = n(b'\xF0\x9F\x9A\x9F')
    MOUNTAIN_CABLEWAY = n(b'\xF0\x9F\x9A\xA0')
    AERIAL_TRAMWAY = n(b'\xF0\x9F\x9A\xA1')
    ROWBOAT = n(b'\xF0\x9F\x9A\xA3')
    VERTICAL_TRAFFIC_LIGHT = n(b'\xF0\x9F\x9A\xA6')
    PUT_LITTER_IN_ITS_PLACE_SYMBOL = n(b'\xF0\x9F\x9A\xAE')
    DO_NOT_LITTER_SYMBOL = n(b'\xF0\x9F\x9A\xAF')
    POTABLE_WATER_SYMBOL = n(b'\xF0\x9F\x9A\xB0')
    NON_POTABLE_WATER_SYMBOL = n(b'\xF0\x9F\x9A\xB1')
    NO_BICYCLES = n(b'\xF0\x9F\x9A\xB3')
    BICYCLIST = n(b'\xF0\x9F\x9A\xB4')
    MOUNTAIN_BICYCLIST = n(b'\xF0\x9F\x9A\xB5')
    NO_PEDESTRIANS = n(b'\xF0\x9F\x9A\xB7')
    CHILDREN_CROSSING = n(b'\xF0\x9F\x9A\xB8')
    SHOWER = n(b'\xF0\x9F\x9A\xBF')
    BATHTUB = n(b'\xF0\x9F\x9B\x81')
    PASSPORT_CONTROL = n(b'\xF0\x9F\x9B\x82')
    CUSTOMS = n(b'\xF0\x9F\x9B\x83')
    BAGGAGE_CLAIM = n(b'\xF0\x9F\x9B\x84')
    LEFT_LUGGAGE = n(b'\xF0\x9F\x9B\x85')
    EARTH_GLOBE_EUROPE_AFRICA = n(b'\xF0\x9F\x8C\x8D')
    EARTH_GLOBE_AMERICAS = n(b'\xF0\x9F\x8C\x8E')
    GLOBE_WITH_MERIDIANS = n(b'\xF0\x9F\x8C\x90')
    WAXING_CRESCENT_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x92')
    WANING_GIBBOUS_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x96')
    LAST_QUARTER_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x97')
    WANING_CRESCENT_MOON_SYMBOL = n(b'\xF0\x9F\x8C\x98')
    NEW_MOON_WITH_FACE = n(b'\xF0\x9F\x8C\x9A')
    LAST_QUARTER_MOON_WITH_FACE = n(b'\xF0\x9F\x8C\x9C')
    FULL_MOON_WITH_FACE = n(b'\xF0\x9F\x8C\x9D')
    SUN_WITH_FACE = n(b'\xF0\x9F\x8C\x9E')
    EVERGREEN_TREE = n(b'\xF0\x9F\x8C\xB2')
    DECIDUOUS_TREE = n(b'\xF0\x9F\x8C\xB3')
    LEMON = n(b'\xF0\x9F\x8D\x8B')
    PEAR = n(b'\xF0\x9F\x8D\x90')
    BABY_BOTTLE = n(b'\xF0\x9F\x8D\xBC')
    HORSE_RACING = n(b'\xF0\x9F\x8F\x87')
    RUGBY_FOOTBALL = n(b'\xF0\x9F\x8F\x89')
    EUROPEAN_POST_OFFICE = n(b'\xF0\x9F\x8F\xA4')
    RAT = n(b'\xF0\x9F\x90\x80')
    MOUSE = n(b'\xF0\x9F\x90\x81')
    OX = n(b'\xF0\x9F\x90\x82')
    WATER_BUFFALO = n(b'\xF0\x9F\x90\x83')
    COW = n(b'\xF0\x9F\x90\x84')
    TIGER = n(b'\xF0\x9F\x90\x85')
    LEOPARD = n(b'\xF0\x9F\x90\x86')
    RABBIT = n(b'\xF0\x9F\x90\x87')
    CAT = n(b'\xF0\x9F\x90\x88')
    DRAGON = n(b'\xF0\x9F\x90\x89')
    CROCODILE = n(b'\xF0\x9F\x90\x8A')
    WHALE = n(b'\xF0\x9F\x90\x8B')
    RAM = n(b'\xF0\x9F\x90\x8F')
    GOAT = n(b'\xF0\x9F\x90\x90')
    ROOSTER = n(b'\xF0\x9F\x90\x93')
    DOG = n(b'\xF0\x9F\x90\x95')
    PIG = n(b'\xF0\x9F\x90\x96')
    DROMEDARY_CAMEL = n(b'\xF0\x9F\x90\xAA')
    BUSTS_IN_SILHOUETTE = n(b'\xF0\x9F\x91\xA5')
    TWO_MEN_HOLDING_HANDS = n(b'\xF0\x9F\x91\xAC')
    TWO_WOMEN_HOLDING_HANDS = n(b'\xF0\x9F\x91\xAD')
    THOUGHT_BALLOON = n(b'\xF0\x9F\x92\xAD')
    BANKNOTE_WITH_EURO_SIGN = n(b'\xF0\x9F\x92\xB6')
    BANKNOTE_WITH_POUND_SIGN = n(b'\xF0\x9F\x92\xB7')
    OPEN_MAILBOX_WITH_RAISED_FLAG = n(b'\xF0\x9F\x93\xAC')
    OPEN_MAILBOX_WITH_LOWERED_FLAG = n(b'\xF0\x9F\x93\xAD')
    POSTAL_HORN = n(b'\xF0\x9F\x93\xAF')
    NO_MOBILE_PHONES = n(b'\xF0\x9F\x93\xB5')
    TWISTED_RIGHTWARDS_ARROWS = n(b'\xF0\x9F\x94\x80')
    CLOCKWISE_RIGHTWARDS_AND_LEFTWARDS_OPEN_CIRCLE_ARROWS = n(b'\xF0\x9F\x94\x81')
    CLOCKWISE_RIGHTWARDS_AND_LEFTWARDS_OPEN_CIRCLE_ARROWS_WITH_CIRCLED_ONE_OVERLAY = n(b'\xF0\x9F\x94\x82')
    ANTICLOCKWISE_DOWNWARDS_AND_UPWARDS_OPEN_CIRCLE_ARROWS = n(b'\xF0\x9F\x94\x84')
    LOW_BRIGHTNESS_SYMBOL = n(b'\xF0\x9F\x94\x85')
    HIGH_BRIGHTNESS_SYMBOL = n(b'\xF0\x9F\x94\x86')
    SPEAKER_WITH_CANCELLATION_STROKE = n(b'\xF0\x9F\x94\x87')
    SPEAKER_WITH_ONE_SOUND_WAVE = n(b'\xF0\x9F\x94\x89')
    BELL_WITH_CANCELLATION_STROKE = n(b'\xF0\x9F\x94\x95')
    MICROSCOPE = n(b'\xF0\x9F\x94\xAC')
    TELESCOPE = n(b'\xF0\x9F\x94\xAD')
    CLOCK_FACE_ONE_THIRTY = n(b'\xF0\x9F\x95\x9C')
    CLOCK_FACE_TWO_THIRTY = n(b'\xF0\x9F\x95\x9D')
    CLOCK_FACE_THREE_THIRTY = n(b'\xF0\x9F\x95\x9E')
    CLOCK_FACE_FOUR_THIRTY = n(b'\xF0\x9F\x95\x9F')
    CLOCK_FACE_FIVE_THIRTY = n(b'\xF0\x9F\x95\xA0')
    CLOCK_FACE_SIX_THIRTY = n(b'\xF0\x9F\x95\xA1')
    CLOCK_FACE_SEVEN_THIRTY = n(b'\xF0\x9F\x95\xA2')
    CLOCK_FACE_EIGHT_THIRTY = n(b'\xF0\x9F\x95\xA3')
    CLOCK_FACE_NINE_THIRTY = n(b'\xF0\x9F\x95\xA4')
    CLOCK_FACE_TEN_THIRTY = n(b'\xF0\x9F\x95\xA5')
    CLOCK_FACE_ELEVEN_THIRTY = n(b'\xF0\x9F\x95\xA6')
    CLOCK_FACE_TWELVE_THIRTY = n(b'\xF0\x9F\x95\xA7')
