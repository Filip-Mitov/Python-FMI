import string


def ceaser_output(number):
    def accepter(func):
        def decorated(*args):
            plain_letters = [symbol for symbol in string.ascii_uppercase]
            cipher_letters = [plain_letters[(index+number)%26]
                              for index in range(26)]
            combined_letters = dict(zip(plain_letters, cipher_letters))
            func_returned = func(*args)
            cipher_text = ""
            for one_symbol in func_returned:
                if one_symbol.isalpha():
                    cipher_text += combined_letters[one_symbol.upper()]
                else:
                    cipher_text += one_symbol
            return cipher_text
        return decorated
    return accepter


def ceaser_input(number, function):
    def accepter(func):
        def decorated(*args):
            corrected_arguments = []
            letters = [symbol for symbol in string.ascii_uppercase]
            cipher_letter = [letters[(index+number) % 26]
                             for index in range(26)]
            combined_letters = dict(zip(letters, cipher_letter))
            for one_arg in args:
                if function(args.index(one_arg)):
                    cipher_text = ""
                    for one_symbol in one_arg:
                        if one_symbol.isalpha():
                            cipher_text += combined_letters[one_symbol.upper()]
                        else:
                            cipher_text += one_symbol
                    corrected_arguments.append(cipher_text)
                else:
                    corrected_arguments.append(one_arg)

            return func(*tuple(corrected_arguments))
        return decorated
    return accepter