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
    return 1

def vld_lname(strpiece):
    return 1

def vld_sepin(strpiece):
    return 1

def vld_paswd(strpiece):
    return 1