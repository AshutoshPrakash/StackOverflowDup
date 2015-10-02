# StackOverflowDup
Automated duplicate question finding in stack overflow using supervised  approaches

Stack overflow is one of the most popular community Q & A sites that people use for solving programming related queries. The site has become so popular that it has a become a repository of huge questions. Often newbies for a particular language or technology finds it difficult to spot already answered questions that can solve their problems, owing to lack of a rich vocabulary related to the particular language. This leads to people posting duplicate questions. The community have a very strict guidelines and have a very active volunteer group to monitor such activities, who will manually label duplicate questions. We have obtained such duplicate questions from the Stack Overflow dump. In this project we will be applying some supervised machine learning techniques to model a classifier that can predict whether there is a duplicate question already in the stack overflow corpus, if a new question along with its description contents are given. We will also be trying some IR related methods that are recently being used in question retrieval.

#Finding Tags from questions.txt
python find_tag.py

# Generating Plots
Pre-Install:
sudo apt-get install python-scipy && sudo apt-get install python-matplotlib

#1. Word Count for questions in each category
	python question_word_count.py total
	For avegare
	python question_word_count.py average
#2. Word Count for questions in each category excluding Stop Words
	python question_word_count_no_stop_word.py total
	For avegare
	python question_word_count_no_stop_word.py average
#3. Word Count for Description in each category
	python description_word_count.py original
	python description_word_count.py onevote
	python description_word_count.py fourvote
	for average
	python description_word_count.py average
	and combined
	python description_word_count.py total
#4. Word Count Ranges for description in each category
	python description_word_range.py original
	python description_word_range.py onevote
	python description_word_range.py fourvote

