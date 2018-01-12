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
	#implementing harmonic mean model HMM
	#
	#
	speech_database_directory="./speech_tags"
	break_points=[" ","\t",",",".","?","!",":",";"]
	print "parsing the content of sentence: kindly type the sentence"
	coordinating_conjunctions=['and','but','or','nor','so','then','yet']
			
        list_of_tag_objects=reading_directory_files(speech_database_directory)
        
        
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



if __name__ == "__main__": main()
