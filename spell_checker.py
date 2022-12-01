# pip install autocorrect

import autocorrect as autospell

check = autospell.Speller(lang='en').spell('speling')
print(check)
