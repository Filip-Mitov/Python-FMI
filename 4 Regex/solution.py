import re


class Patterns():

    user_name = '[\w\d][\w\d+\.-]{0,198}'
    second_level_domain = '([\w\d-]{,60}[\w\d]\.)+'
    top_level_domain = '\w{2,3}(\.\w{2,3})?'
    hostname = second_level_domain + top_level_domain
    email = '\\b' + user_name + '@' + hostname + '\\b'

    phone_prefix = '(\\b(?:00\d{1,2}){1}|\\b0[1-9]|\+[1-9]\d{1,2})'
    international_prefix = '(\\b(?:00\d{1,2}){1}|\+[1-9]\d{1,2})'
    phone_digits = '[-\)\( ]{0,2}(?:\d[-\)\( ]{0,2}){6,10}\d\\b'
    international_phone = '('+international_prefix + phone_digits+')'
    phone = phone_prefix + phone_digits

    ip_octet = '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    ip_address = (ip_octet + '\.') * 3 + ip_octet

    number = '-?0$|((^0|^-?[1-9])\d*(\.\d+)?$)'

    integer = '-?0$|((^0|^-?[1-9])\d*$)'

    date = '\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])'

    time = '([01]\d|2[0-3]):[0-5][0-9]:[0-5][0-9]'

    date_and_time = date + '( |T)' + time


class Validations(Patterns):

    def __init__(self):
        pass

    def matcher(regex, string):
        return False if re.match(regex, string) is None else True

    def searcher(regex, string):
        return False if re.search(regex, string) is None else True

    def is_email(value):
        return Validations.searcher(Patterns.email, value)

    def is_phone(value):
        return Validations.searcher(Patterns.phone, value)

    def is_hostname(value):
        return Validations.matcher(Patterns.hostname, value)

    def is_ip_address(value):
        return Validations.matcher(Patterns.ip_address, value)

    def is_number(value):
        return Validations.matcher(Patterns.number, value)

    def is_integer(value):
        return Validations.matcher(Patterns.integer, value)

    def is_date(value):
        return Validations.matcher(Patterns.date, value)

    def is_time(value):
        return Validations.matcher(Patterns.time, value)

    def is_datetime(value):
        return Validations.matcher(Patterns.date_and_time, value)


class PrivacyFilter(Patterns):

    def __init__(self, value):
        self.preserve_phone_country_code = False
        self.preserve_email_hostname = False
        self.partially_preserve_email_username = False
        self.text = value

    def filtered(self):
        filtered_information = self.text[:]

        if self.preserve_email_hostname == False and self.partially_preserve_email_username == False:
            filtered_information = re.sub(
                Patterns.email, '[EMAIL]', filtered_information
            )
        elif self.preserve_email_hostname == True and \
             self.partially_preserve_email_username == False:
            filtered_information = re.sub(
                Patterns.user_name+'@', '[FILTERED]@', filtered_information
            )
        elif self.preserve_email_hostname == False and \
             self.partially_preserve_email_username == True:
            match = re.findall(Patterns.user_name+'@', filtered_information)
            for element in match:
                filtered_information = re.sub(
                    element, element[:3]+'[FILTERED]@', filtered_information
                )
        elif self.preserve_email_hostname == True and \
             self.partially_preserve_email_username == True:
            filtered_information = re.sub(
                Patterns.user_name+'@', '[FILTERED]@', filtered_information
            )

        if self.preserve_phone_country_code == True:
            all_matches = re.findall(
                Patterns.international_phone, filtered_information
            )
            for one_match in all_matches:
                filtered_information = filtered_information.replace(
                    one_match[0], one_match[1] + ' [FILTERED]'
                )
            filtered_information = re.sub(
                Patterns.phone, '[PHONE]', filtered_information
            )
        elif self.preserve_phone_country_code == False:
            filtered_information = re.sub(
                Patterns.phone, '[PHONE]', filtered_information
            )

        return filtered_information