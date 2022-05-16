
# 001 문자열을 줄여 표시하려면? - textwrap.shorten

import textwrap

print(textwrap.shorten("Life is too short, you need python", width=15))
print(textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15, placeholder='***'))