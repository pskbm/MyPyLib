
# 002 긴 문장을 줄 바꿈하려면? - textwrap.wrap

import textwrap

long_text = 'Life is too short, you need python. ' * 10
result = textwrap.wrap(long_text, width=70)

print(result)
print('\n'.join(result))
# '\n'.join(List)는 리스트 요소 사이에 줄 바꿈 문자를 넣어 하나로 합친다. 리스트가 아닌 문자열이나 튜플에도 적용할 수 있다.
print(result[1])
print(type(result))

# 참고로 textwrap.fill() 함수를 사용하면 이 과정을 한 번으로 줄일 수 있다.
result1 = textwrap.fill(long_text, width=70)
print(result1)