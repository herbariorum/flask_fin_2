
class Uteis:

    @staticmethod
    def is_only_number(s):
        return ''.join(filter(lambda i: i if i.isdigit() else None, s))
    
    @staticmethod
    def check_email(email):
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if re.search(email_regex, email):
            return True
        return False
    
    @staticmethod
    def is_not_blank(s):
        return bool(s and not s.isspace())