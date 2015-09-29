import MySQLdb

db = MySQLdb.connect("localhost","root","ashu","stack_overflow" )
cursor = db.cursor()
cursor.execute("select name from tag;")
data = cursor.fetchall()
db.close()

tags = [element for tupl in data for element in tupl] #flattening a nested structure

with open("english_stop_words.txt") as f:
    stop_words = f.readlines()
stop_words = [line.rstrip('\n') for line in stop_words]

with open("questions.txt") as f2:
    questions = f2.readlines()
    
output_tags = []
for q in questions:
	#print "\n# Question found :",q
	q2 = q.replace("\n","")
	#splitting a string into list of words and removing special symbols
	q = q.replace("\n","").replace(".","").replace("-","").replace("'","").replace("?","").lower().split()
	
	for s in stop_words:
		if s.lower() in q:
			q[:] = [item for item in q if item != s.lower()]#removes all instances
	#print "- After stop_word removal :",q
	ll = []
	for q1 in q:
		if q1 in tags:
			#print "tag found : ",q1
			ll.append(q1)
	output_tags.append({'q':q2 ,'tags':ll})

print output_tags
