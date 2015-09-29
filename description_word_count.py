from __future__ import division
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import sys

db = MySQLdb.connect("localhost","root","ashu","stack_overflow" )
cursor = db.cursor()

r =  '-'
r2 = '+'
r3 = '|'


def modify( p ):
	v = []
   	if ' ' in p[0][0].replace(r,"").replace(r2,"").replace(r3,"").split(' '):
		v = p[0][0].replace(r,"").replace(r2,"").replace(r3,"").split(' ').remove(' ')
	else :
		v = p[0][0].replace(r,"").replace(r2,"").replace(r3,"").split(' ')
	if '' in v:
		v = v.remove('')
	
	return v


original_count = {}
vote1_count  = {}
vote4_count = {}
o = 0
v1 = 0
v4 = 0

with open("originalQuestions.txt") as f2:
	for line in f2:
		cursor.execute("select body_text from post where id ="+line+";")
		p = cursor.fetchall()
		if len(p) !=0:
			v = modify(p)
			if v!=None:
				if len(v) in original_count:
					original_count[len(v)] += 1
					o+=1
				else:
					original_count[len(v)] = 1

with open("dupWithVote1.txt") as f:
    for line in f:
		cursor.execute("select body_text from post where id ="+line+";")
		p = cursor.fetchall()
		if len(p) !=0:
			v = modify(p)
			if v!=None:
				if len(v) in vote1_count:
					vote1_count[len(v)] += 1
					v1+=1
				else:
					vote1_count[len(v)] = 1

with open("dupWithVoteGrtr4.txt") as f3:
    for line in f3:
		cursor.execute("select body_text from post where id ="+line+";")
		p = cursor.fetchall()
		if len(p) !=0:
			v = modify(p)
			if v!=None:
				if len(v) in vote4_count:
					vote4_count[len(v)] += 1
					v4 += 1
				else:
					vote4_count[len(v)] = 1

db.close()

# with open("1.txt", "a") as myfile:
# 	myfile.write("")

# print original_count
# print vote1_count
# print vote4_count

arr_original = []
arr_vote1 = []
arr_vote4 = []
keys = []
orig_avg = 0
vote1_avg = 0
vote4_avg = 0

n_groups = max(original_count.keys()[-1],vote1_count.keys()[-1],vote4_count.keys()[-1])
for i in range(1,n_groups+1):
	if i in original_count:
		arr_original.insert(i,original_count[i]/o)
		orig_avg += i*original_count[i]
	else :
		arr_original.insert(i,0)

	if i in vote1_count:
		arr_vote1.insert(i,vote1_count[i]/v1)
		vote1_avg += i*vote1_count[i]
	else :
		arr_vote1.insert(i,0)

	if i in vote4_count:
		arr_vote4.insert(i,vote4_count[i]/v4)
		vote4_avg += i*vote4_count[i]
	else :
		arr_vote4.insert(i,0)

	keys.insert(i,i)

# print arr_original
# print arr_vote1
# print arr_vote4

index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.4

if str(sys.argv[1])=='original':
	rects1 = plt.bar(index, tuple(arr_original), bar_width,alpha=opacity,color='b',label='Original Questions')
elif str(sys.argv[1])=='onevote':
	rects2 = plt.bar(index + bar_width, tuple(arr_vote1), bar_width,alpha=opacity,color='r',label='Duplicate Question with vote=1')
elif str(sys.argv[1])=='fourvote':
	rects3 = plt.bar(index + bar_width+ bar_width, tuple(arr_vote4), bar_width,alpha=opacity,color='c',label='Duplicate Question with vote>4')
elif str(sys.argv[1])=='average':
	rects1 = plt.bar(np.arange(3), (orig_avg/o, vote1_avg/v1, vote4_avg/v4), 0.8 ,alpha=0.4,color='b',label="Average")
	plt.title('Average Word Count Category-wise')
	plt.xlabel('Categories')
	plt.ylabel('Average No. of Words')
	plt.xticks(np.arange(3)+ bar_width+bar_width, ('original','vote = 1','vote > 4'))
else: 
	rects1 = plt.bar(index, tuple(arr_original), bar_width,alpha=opacity,color='b',label='Original Questions')
	rects2 = plt.bar(index + bar_width, tuple(arr_vote1), bar_width,alpha=opacity,color='r',label='Duplicate Question with vote=1')
	rects3 = plt.bar(index + bar_width+ bar_width, tuple(arr_vote4), bar_width,alpha=opacity,color='c',label='Duplicate Question with vote>4')

	plt.title('Questions Description Word Count')
	plt.xlabel('Word Count')
	plt.ylabel('Fraction of Questions')

	plt.xticks(index + bar_width, tuple(keys))

plt.legend()
plt.tight_layout()
plt.show()