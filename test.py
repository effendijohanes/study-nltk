import nltk
from nltk.tree import Tree as tree

t = tree.fromstring("( (S (NP (PRP I)) (VP (VBP 'm) (NP (NP (DT a) (JJ contemporary) (NN artist)) (PP (IN with) (NP (NP (DT a) (NN bit)) (PP (IN of) (NP (DT an) (JJ unexpected) (NN background))))))) (. .)) )")
#print t
#dir(t)
#print t.leaves()


t1 = tree.fromstring("( S (NP (PRP I))(VP (VBP eat) (NN rice)) )")

def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t)
    else:
        # Now we know that t.node is defined
        print('(', t.label())
    	for child in t:
    		if child.label() == 'NP':
        		traverse(child)

        print(')')	
        
def compare_similar(t1, t2):
	print "---------------------------"
	res_t1 = check_label_available(t1)
	res_t2 = check_label_available(t2)

	print res_t1
	print res_t2

	if res_t1==0 and res_t2==0:
		print "masuk base case"
		return 1

	if res_t1!=0 and res_t2!=0:
		if t1.label() == t2.label() and len(t1) == len(t2):
			for index in range(len(t1)):
				compare_similar(t1[index], t2[index])
		else:
			return 0
	return 0


def check_label_available(t):
	try:
		t.label()
	except AttributeError:
		return(0)
	else:
		return(t)

#traverse(t1)
if compare_similar(t1,t1):
	print "same"
else:
	print "woy"