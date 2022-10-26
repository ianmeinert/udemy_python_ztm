import re

pattern = re.compile(r"([a-zA-Z0-9$%#@]{8,})")
password = r'$up3r$3cr3T'
match = pattern.fullmatch(password)

if match is not None:
    print(match.string)
else:
    print("Failed to match requirements")
