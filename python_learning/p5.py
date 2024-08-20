'''
Accept average score from the student of his exam and print his result as follows:

0 to 49 is Fail
50 to 74 is second class
75 to 90 is first class
91 to 100 is distinction
Also check for invalid score
'''

avg_score = int(input('Enter average score for results: '))

 
if avg_score >= 91 and avg_score <= 100:
    print('Result is Distiction')  
elif avg_score >= 75 and avg_score <= 90:
    print('Result is First class')
elif avg_score >=50 and avg_score <= 74:
    print('Result is Second class')    
elif avg_score >= 0 and avg_score <= 49:
    print('Result is Fail')
else:
    print('Invalid score!')

