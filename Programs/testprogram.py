

def inputNumbers():
	inputs = raw_input('Enter Scores:-->').split(',')
	scores = map(int, inputs)
	return scores;
def editScore(x):
	for n in range(0,len(x)):
		x[n] = x[n] * 4 + 8
		file.write("%d\n" % x[n])
	return None

file = open('testscores.txt',"w")

y = inputNumbers();

x = editScore(y)

file.close()

