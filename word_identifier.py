




def main():
	string1=raw_input()	
	#load_nouns()
	lexical_analyzer(string1)
def lexical_analyzer(string1):
	print string1
	word=""
	list_of_noun=open('nounlist_1.txt','r')
	list_of_noun=list_of_noun.read()
	print list_of_noun
	list_noun=[]
	for character in list_of_noun:
		if character == "\n" and word != "":
			list_noun.append(word)
			word=""
		else:
			word+=character
	word=""	
	list_noun=sorted(list_noun)
	for character in string1:
		if character==" ":
			for character in word:
				print character	
			word=""
		else:
			word+=character	

if __name__ == "__main__":main()
