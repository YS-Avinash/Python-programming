'''
python function to generate and return the list of all possible sentences created from the given lists of Subject, Verb and Object.
Sample Input :	
  subjects=["I", "You"]
  verbs=["Play", "Love"]
  objects=["Hockey","Football"]
  
Expected Output:
  I Play Hockey
  I Play Football
  I Love Hockey
  I Love Football
  You Play Hockey
  You Play Football
  You Love Hockey
  You Love Football
'''
def generate_sentences(subjects,verbs,objects):
	sentence_list=[]
	for s in subjects:
	    for v in verbs:
	        for o in objects:
	            sentence_list.append(s+" "+v+" "+o)
	return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
