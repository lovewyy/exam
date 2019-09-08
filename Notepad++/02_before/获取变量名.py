aaa = '23asa'
loc = locals()

def get_variable_name(variable):
    for key in loc:
        if loc[key] == variable:
            return key

print(get_variable_name(aaa))


