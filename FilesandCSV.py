#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
filname=open('travel_plans.txt','r')
lis=list()
for line in filname:
    c=len(line)
    lis.append(c)
num=sum(lis)
print(num)

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
filname=open('emotion_words.txt','r')
lis=list()
for line in filname:
    u=line.strip()
    v=u.split()
    a=len(v)
    lis.append(a)
num_words=sum(lis)
print(num_words)

#Assign to the variable num_lines the number of lines in the file school_prompt.txt
filname=open('school_prompt.txt','r')
count=0
for line in filname:
    count=count+1
num_lines=count
print(num_lines)

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars
filname=open('school_prompt.txt','r')
h=filname.read()
beginning_chars=h[:30]
print(beginning_chars)

#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
filname=open('school_prompt.txt','r')
lis=list()
for line in filname:
    u=line.split()
    a=u[2]
    lis.append(a)
three=lis
print(three)

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt
filname=open('emotion_words.txt','r')
lis=list()
for line in filname:
    u=line.split()
    a=u[0]
    lis.append(a)
emotions=lis
print(emotions)
#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars
filname=open('travel_plans.txt','r')
h=filname.read()
first_chars=h[:33]
print(first_chars)
#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
filname=open('school_prompt.txt','r')
lis=list()
for line in filname:
    u=line.strip()
    a=u.split()
    for x in a:
        if 'p' in x:
            lis.append(x)
p_words=lis   
print(p_words)
    
    
