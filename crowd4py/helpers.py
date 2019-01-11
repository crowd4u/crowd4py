import re


def attach_prefix(string):
    prefix = '_FACT1___'
    pattern = '^_FACT1___|^_Fact1_|^_'
    match = re.search(pattern=pattern, string=string)
    return string if match else prefix + string


def detach_prefix(string):
    pattern = '^_FACT1___'
    detach_string = re.sub(pattern=pattern, repl='', string=string)
    return detach_string
