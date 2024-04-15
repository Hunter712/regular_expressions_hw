import re

str = '''
The zebra races across the savannah.
The wizard conjured a dazzling display of magic.
The maze was a challenge to navigate, with twists and turns at every corner.
'''

task1 = re.findall(r'\w+z\w+', str)

for match in task1:
    print(match)

# ----------------------
str = '''
192.168.001.001
010.000.000.001
000172.016.254.001
255.255.255.000
008.008.008.008
'''

task2 = re.sub(r'^0{1,3}', r'', str, flags=re.MULTILINE)
print(task2)

# ----------------------
str = '''
The zebra races across the savannah.
The wizard conjured a dazzling display of magic.
The zebras races across the savannah.
'''

task3 = re.finditer(r"\bze\w+", str)

for match in task3:
    print("word -", match.group(0), "\nstart position -", match.start(), "\nend position -", match.end())

# ----------------------
str = '''
2024-04-15 date format 1985-05-25 date format
'''


def replace_date(match):
    matched_date = match.group(0)
    modified_date = matched_date.split("-")
    modified_date = modified_date[::-1]
    modified_date = '-'.join(modified_date)
    return modified_date


task4 = re.sub(r'\d{4}-\d{2}-\d{2}', replace_date, str)
print(task4)

# ----------------------
str = '''
The zebr races across the savannah.
The wiza conjured a dazzling display of magic.
The zebras races across the savannah.
'''

task5 = re.findall(r'\b\w{3,5}\b', str)

for match in task5:
    print(match)

# ----------------------
str = '''
phoneNumber
emailClient
socialMedia
webBrowser
'''


def replace_date(match):
    first_part = match.group(1)
    second_part = match.group(2)
    second_part = "_" + second_part.lower()
    return first_part + second_part


task6 = re.sub(r'(\w+)([A-Z]\w+)', replace_date, str)
print(task6)

# ----------------------
str = '''
Yesterday, Jack quickly ran to the store to buy some groceries. 
He carefully picked out the freshest fruits and vegetables.
'''

task7 = re.finditer(r"\w+ly\b", str)

for match in task7:
    print("word -", match.group(0), "\nstart position -", match.start(), "\nend position -", match.end())

# ----------------------
str = '''
Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready.
'''


def replace_date(match):
    matched_date = match.group(0)
    modified_date = matched_date.replace(" ", "")
    return modified_date


task8 = re.sub(r'\d+\s\d+', replace_date, str)
print(task8)
