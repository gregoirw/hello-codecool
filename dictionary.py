import csv
start=1
lpd={'function' : ("A function is a block of organized reusable code that is used to perform a single related action. Functions provide better modularity for your application and a high degree of code reusing.", "source: www.tutorialspoint.com/python/python_functions.htm",),
        'parameter' : ("A named entity in a function (or method) definition that specifies an argument (or in some cases arguments) that the function can accept.","source: docs.python.org/3/glossary.html",),
        'variable' : ("A variable is something that holds a value that may change. In simplest terms a variable is just a box that you can put stuff in. ","source: en.wikibooks.org/wiki/Python_Programming/Variables_and_Strings",),
        'argument' : ("An argument is simply a value provided to a function when you call it","source: stackoverflow.com/questions/14924825/what-are-arguments-in-python"),
        'dictionary' : ("In a dictionary you have an 'index' of words and for each of them a definition. In python the word is called a 'key' and the definition a 'value'. The values in a dictionary aren't numbered - tare similar to what their name suggests - a dictionary. In a dictionary you have an 'index' of words and for each of them a definition. In python the word is called a 'key' and the definition a 'value'. The values in a dictionary aren't numbered - they aren't in any specific order either - the key does the same thing. You can add remove and modify the values in dictionaries.","source: sthurlow.com/python/lesson06/",),
        'tuple' : ("Tuples are just like lists but you can't change their values. The values that you give it first up are the values that you are stuck with for the rest of the program. Again each value is numbered starting from zero for easy reference.","source: sthurlow.com/python/lesson06/",),
        'ASCII' : (" abbreviated from American Standard Code for Information Interchange is a character encoding standard (the Internet Assigned Numbers Authority (IANA) prefers the name US-ASCII). ASCII codes represent text in computers telecommunications equipment and other devices. Most modern character-encoding schemes are based on ASCII although they support many additional characters.","source:https://en.wikipedia.org/wiki/ASCII",),
        'module' : ("A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.","source: docs.python.org/3/tutorial/modules.html",)}
CSV ="\n".join([k+','+",".join(v) for k,v in lpd.items()])
#print(CSV) #You can store this string variable to file as you wish
with open("filename.csv", "w") as file:
    file.write(CSV)
#with open('dict.csv', 'w') as csv_file:
#    writer = csv.writer(csv_file)
#    for key, value in lpd.items():
#       writer.writerow([key, value])
while start==1:
    while True:
        try:
            menu=int(input('''Dictionary for a little programmer.
                        1) search explanation by appellation *
                        2) add new definition
                        3) show all appellations alphabetically
                        4) show available definitions by first letter of appellation **
                        0) exit) \n'''))
            check=int(menu)
            break
        except ValueError:
            print("Wrong input!!!")
            True
        except IndexError:
            print("Wrong input!!!")
            True

    if menu==1:
        xyz=input("Please enter the word you want to search for\n")
        print(lpd.get(xyz))
    elif menu==2:
        key_input=input("Please enter the appellation:")
        definition_input=input("Please enter the definition:")
        source_input=input("please enter the source of your definition:")
        lpd[key_input] = (definition_input,source_input,)
        CSV ="\n".join([k+','+",".join(v) for k,v in lpd.items()])
        #print(CSV) #You can store this string variable to file as you wish
        with open("filename.csv", "w") as file:
            file.write(CSV)
        #print("good")
    elif menu==3:
        d={}

        for row in csv.reader(open('filename.csv')):
            d['%s' % row[0]] = {'definition': row[1], 'source': row[2]}
        for key in sorted(d):
            print("%s: %s \n" % (key, d[key]))
    elif menu==4:
        print("Sorry this isn't available yet !!! Check out later (or never :D )\n")
    elif menu==0:
        start=0
    else:
        print("Wrong input!!!")
