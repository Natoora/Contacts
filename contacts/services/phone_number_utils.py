import os
import re

import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

from contacts.models import Contact


def get_country_code():
    """
    Temporary solution, remove when we have a
    company model which sets the country code.

    :return: Code for tel number parsing.
    """
    code = os.environ.get("COUNTRY_CODE", None)

    return code


def possibly_valid(tel):
    """
    Basic number validity checks, length and pattern etc.
    """
    valid = True
    tel = re.sub("[-. ()]", "", tel)
    if len(tel) < 7 or len(tel) > 20:
        valid = False
    if not re.match("^[+]?[0-9]{7,20}$", tel):
        valid = False
    return valid


def parse_phone_number(tel):
    """Try to parse telephone number in E164 standard format (https://en.wikipedia.org/wiki/E.164).

    :param tel: str, phone number to parse.
    :return: Bool, True if parse successful.  Str, phone number parsed or not.
    """
    parsed = False
    if possibly_valid(tel):
        try:
            tel = "+" + tel[2:] if tel.startswith("00") else tel

            try:
                parsed_tel = phonenumbers.parse(tel)
                if phonenumbers.is_valid_number(
                    parsed_tel
                ) and phonenumbers.is_possible_number(parsed_tel):
                    tel = phonenumbers.format_number(
                        parsed_tel, phonenumbers.PhoneNumberFormat.E164
                    )
                    return True, tel
            except NumberParseException:
                parsed = False

            try:
                parsed_tel = phonenumbers.parse(tel, get_country_code())
                if phonenumbers.is_valid_number(
                    parsed_tel
                ) and phonenumbers.is_possible_number(parsed_tel):
                    tel = phonenumbers.format_number(
                        parsed_tel, phonenumbers.PhoneNumberFormat.E164
                    )
                    return True, tel
            except NumberParseException:
                parsed = False
                print(tel)

        except Exception as e:
            print(e)

    return parsed, tel


def standardise_contacts_phonenumbers(save=False, cnts=None):
    """Standardise contact phone numbers.

    If the phone number can't be parsed, add the number to contact notes.
    """
    cnts = cnts or Contact.objects.all()
    for c in cnts:
        if c.mobile:
            parsed, tel = parse_phone_number(c.mobile)
            if parsed:
                c.mobile = tel
            else:
                c.mobile = None
                if tel != "0":
                    c.notes = c.notes + tel if c.notes else tel
        if c.telephone:
            parsed, tel = parse_phone_number(c.telephone)
            if parsed:
                c.telephone = tel
            else:
                if tel != "0":
                    c.notes = c.notes + tel if c.notes else tel
        if save:
            c.save()
