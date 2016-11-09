import nltk
from nltk.tree import Tree as tree

t = tree.fromstring("( (S (NP (PRP I)) (VP (VBP 'm) (NP (NP (DT a) (JJ contemporary) (NN artist)) (PP (IN with) (NP (NP (DT a) (NN bit)) (PP (IN of) (NP (DT an) (JJ unexpected) (NN background))))))) (. .)) )")
#print t
#dir(t)
#print t.leaves()


t1 = tree.fromstring("( S (NP (PRP I))(VP (VBP eat) (NN rice)) )")
t2 = tree.fromstring("(S)")

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
	empty_t1 = check_label_is_empty(t1)
	empty_t2 = check_label_is_empty(t2)

	if (empty_t1 and not empty_t2) or (not empty_t1 and empty_t2):
		return False

	if empty_t1 and empty_t2:
		return True

	if t1.label() != t2.label():
		return False

	same_child = True
	for index in range(len(t1)):
		same_child = same_child and compare_similar(t1[index], t2[index])

	return same_child

def check_label_is_empty(t):
	try:
		t.label()
	except AttributeError:
		return True
	else:
		return False

#traverse(t1)
if compare_similar(t,t):
	print "same"
else:
	print "woy"