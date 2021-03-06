import pickle

def process_vocab(l):
	v = []
	for e in l:
		x = e.split('(')[0]
		x = x.replace('_',' ').lower()
		v.append(x)
	return v

v = pickle.load(open('../concept_vocab.pkl', "rb"))
vd = dict({x.lower().replace('_', ' '):int(k) for k,x in v.items()})

for i in range(5):
	for type in [('test_','.txt'), ('train_', '.txt')]:
		fn = type[0]+str(i)+type[1]
		f = open(type[0]+str(i)+'_index.txt','w')
		for each in open(fn, "r").read().splitlines():
			c = process_vocab(each.strip().split(','))
			a = c[0]
			b = c[1]

			if (vd.get(a) is not None and vd.get(b) is not None):
				f.write(str(vd[a])+','+str(vd[b])+','+c[2]+'\n')
			
			break

		f.close()



