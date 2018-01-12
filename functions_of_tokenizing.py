
class functions_of_parsing:
	def __init__(self):
		print "function of parser"


        def reading_file_into_directory(self, file_name):
		self.list_of_tags=[]
		reader=open(file_name,"r")
                print "reading file"
		feeder=reader.read()
		word=""
		for character in feeder:
			if character=="\n":
				self.list_of_tags.append(word)
				word=""
			else:		
				word+=character


