def convert_temp(temp,unit):
    if unit=='C':
        return temp *9/5 + 32
    elif unit=='F':
        return (temp-32)*5/9
    else:
        return None

print(convert_temp(25,'C' ))