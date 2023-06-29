import re

my_str = "1990-ben születtem"

x = re.findall('\D', my_str)
x = re.findall('ü', my_str)
x = re.findall('.', my_str)
x = re.findall('\.', my_str)

my_str = "indul     a görög aludni"

x = re.search('\s', my_str)

#################################

x = re.split('\s', my_str)


my_str = "eíhgírh42m64zél34mnz3qéq345él3q457n34qé75l4qn"

x = re.sub('\d+', ' ', my_str)

print(x)