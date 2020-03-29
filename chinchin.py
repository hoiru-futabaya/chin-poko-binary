#!/usr/bin/env python
# -*- coding: utf-8 -*-

str_data = ''

print('ちんぽこ変換したい文字列を入力')

str_data = input('>>')

bytes_data = str_data.encode('UTF-8', 'replace').hex()

a = int(bytes_data, 16)

b = bin(a)

chinchin = list(b)

result = ''

for chin in chinchin:

	if chin == '0':
		
		result = result + 'ちん'
			
	else:
		
		result = result + 'ぽこ'
		
print(result)
