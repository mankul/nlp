from speech_tags_objects_and_functions import *
import os

speech_database_directory="./speech_tags"


def reading_directory_files(speech_database_directory):
    list_of_files=os.listdir(speech_database_directory)
    list_of_objects={}
    for files in list_of_files:
        print files
    
        file_path=speech_database_directory+"/"+files
        new_tag=Tags(file_path,files[:-5])
        list_of_objects[files[:-5]]=new_tag
    return list_of_objects

def main():
	#
	#implementing hidden markov model HMM
	#
	#
	speech_database_directory="./speech_tags"
	break_points=[" ","\t",",",".","?","!",":",";"]
	print "parsing the content of sentence: kindly type the sentence"
	coordinating_conjunctions=['and','but','or','nor','so','then','yet']
			
        dict_of_tag_objects=reading_directory_files(speech_database_directory)
        print dict_of_tag_objects
                
        
        #	noun=Noun(speech_database_directory)
	#
	#
	#
	sentence=raw_input()
	#
	#
	word=''
	previous_label=''
	sentence_list={}
        '''
	for character in sentence:
		if character in break_points:
			if word in coordinating_conjunctions:
				previous_label="cc"
			if previous_label=="nn":
				if word in verb_list:
					sentence_list.append(word)
					previous_label="verb"
			elif previous_label=="verb":
				print "yes"	
			word=""
			
		else:
			word+=character

        '''
        word=""
        counter=0
        for character in sentence:

            if character == (" " ) or counter == len(sentence)-1:
                if counter == len(sentence)-1:
                    word+=character
                label=[]
                for tag_obj in dict_of_tag_objects.values():
                    if word in tag_obj.list_of_tags:
                        label.append(tag_obj.tag_name)
                if label != []:
                    print word , label, "\n"
                else:
                    print word, "not in database,, kindly rerun "
                word=""
                counter+=1
            else:
                word+=character
                counter+=1

            

if __name__ == "__main__": main()
