# with open('1_Lectures\Lesson_2\.file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
 
# exit()
colors = ['red', 'green', 'blue']
data = open('1_Lectures\Lesson_2\.file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()


path = '1_Lectures\Lesson_2\.file.txt'
data = open(path, 'r')
for line in data:
 print(line)
data.close()

