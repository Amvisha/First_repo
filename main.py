#def modify_list(lst: list) -> None:
#    lst = lst.copy()
#   lst.append(4)
#   lst.append(5)
#   print(lst)
#
#my_list = [1, 2, 3]
#modify_list(my_list)
#print(my_list)  # виведе: [1, 2, 3]
#hello =  'Hello'
#world = 'World'
#message = 'Write %s %s' % (hello, world)
#print(message)

#hello =  'Hello'
#world = 'World'
#message = 'Write {} {}'.format(hello, world)
#print(message)
"""
age = str(27.95)
message = round(float(age), 2), type(age)
print(message)

value_one = 5
value_two = 7
value_three = -19
summary = 0
summary += abs(value_one)
print(summary)
summary += abs(value_two)
print(summary)
summary += abs(value_three)
print(summary)
"""
sentense_one = 'Hello world'
sentense_two = 'Hello ' + 'world'
print(sentense_one, sentense_two, sep='\n')
print(f'Are sentence equal?',  sentense_one == sentense_two)
print(f'Are sentence identical?',  sentense_one is sentense_two)
print(f'Path the sentence in memory {id(sentense_one)}')
print(f'Path the sentence in memory', id(sentense_two))
