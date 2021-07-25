
thousands = "M{0,3}"
hundreds = "(CD|CD|D?c{0,3})"
tens = "(XC|XL|L?X{0,3})"
digits = "(IX|IV|V?I{0,3})"

regex_pattern = r"%s%s%s%s$" % (thousands,hundreds, tens, digits)    


import re
print(str(bool(re.match(regex_pattern, input()))))