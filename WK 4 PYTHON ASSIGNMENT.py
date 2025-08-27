file = open('random_file.pdf', 'w')  # Open file
file.write('Hello World')            # Write text
file.close()                         # Close file


file=open('MEDS.pdf','w')        # Open file
file.write('distributes to mission hospitals along MSA road \n  icluding Tumutumu,PCEA Chogoria,Chuka and Meru \n  hospitals') # Write text
file.close()    
file=open('MEDS.pdf','r')
content=file.read()
print(content)
file.close()
with open ('random_file.pdf','w') as file:
    data=file.write("I love programming")
    print(data)
    with open('random_file.pdf','r') as file:# overwrites previous work
        content=file.read()
        print(content)
with open('random_file.pdf','a') as file:
        content= file.write("\nI love python programming")
        print(content)
with open('random_file.pdf','r') as file:
        content=file.read()
        print(content)
        file.close()
with open('random_file.pdf','r') as file:
        content=file.readlines()[:1]
        print('Line_one is',content)
        file.close()


try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
finally:
      file.close


with open('input.txt', 'w') as file:
   data= file.writelines([
        "I love programming\n",
        "Python is awesome\n",
        "I am learning JavaScript\n",
        "I am learning HTML\n",
        "I am learning CSS\n"
    ])
print(data)
with open('input.txt', 'r') as file:
    content = file.readline()[:2]
    print(content)

def count_characters(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return len(content)

print(count_characters('input.txt'))

def upper(filename):
     with open('input.txt', 'r') as file:
        data=file.read()
        return data.upper()
print(upper('input.txt'))

with open('output.txt', 'w') as file:
    file.write(str(count_characters('input.txt')) + '\n')  # convert to string
    file.write(upper('input.txt'))  # assuming upper returns string
print('Done')
file.close()

           







