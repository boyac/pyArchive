#ref: http://harrypotter.wikia.com/wiki/Marauder's_Map
import collections
text = 'APT strives to be the ? ? ? ? ? ? ? ? ? ? to unite consulting and technology'
code = '| @ } $ ^ & - # { & * ~ + { & * { & { ~ } ^ ~ & @ ) % & @ } ^ ( ! ^ @ #'
code_n = '|@}$^&-#{&*~'
code_s = '}@&%)@&~^}~{'
code_e = '+{&*{&'
code_w = '#@^!(^' 
code.split(',')
code_n.split(',')
code_e.split(',')
code_s.split(',')
code_w.split(',')
#print collections.Counter(text)
#print len(text)
print len(code)
#print collections.Counter(code)
#print collections.Counter(code_n)

code_nn = []
for i in code_n:
	code_nn.append(str(ord(i)) * 1)

code_ss = []
for i in code_s:
	code_ss.append(str(ord(i) * -1))

code_ee = []
for i in code_e:
	code_ee.append(str(ord(i)) * 1)

code_ww = []
for i in code_w:
	code_ww.append(str(ord(i) * -1))

lon = (code_nn + code_ss)
lat = (code_ee + code_ww)

print lon
print lat
