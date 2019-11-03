import re

def vld_email(strpiece):
    regex = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_phnum(strpiece):
    regex = "^([\+][0-9]{2,3})?[1-9][0-9]{9}$"
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_fname(strpiece):
    regex = "^[A-Z]{3,20}$"
    strpiece = strpiece.upper()
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_lname(strpiece):
    regex = "^[A-Z]{3,20}$"
    strpiece = strpiece.upper()
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_sepin(strpiece):
    regex = "^[0-9]{6}$"
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_paswd(strpiece):
    regex_ezy = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    regex_med = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    regex_hrd = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    # Minimum eight characters, at least one letter and one number
    # Minimum eight characters, at least one uppercase letter, one lowercase letter and one number
    # Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character
    if re.match(regex_ezy, strpiece):
        if re.findall(regex_med, strpiece):
            if re.findall(regex_hrd, strpiece):
                return 3
            else:
                return 2
        else:
            return 1
    else:
        return 0