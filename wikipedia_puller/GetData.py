import os
import sys
import shutil
import wikipedia


#Getting the query from the user
def getQuery():
    tmp = ""
    if(len(sys.argv) > 1):
        tmp = sys.argv[1]
    else:
        print("Enter query: ", end="")
        tmp = input()
    return tmp

#Grabs data from wikipedia search
def pullData(query):
    retVal = ""
    try:
        tmp = wikipedia.search(query)[1]
        retVal = wikipedia.page(tmp).content
    except:
        retVal = "dead"
    return retVal

#Writes to file
def writer(filename, data):
    file = open(filename, "w")
    file.write(data)
    file.write("\n")
    file.close()

#Move dump.txt files into dumpfiles directory
def relocate(filename):
    path = os.getcwd()
    path += "/"
    src = path + filename
    dest = path + "dumpfiles/" + filename
    shutil.move(src, dest)

#Reads data queries from file
def read():
    arr = []
    for line in open("queries.txt"):
        line = line.split()[0]
        arr.append(line)
    return arr

#Assistant to Driver
def execute(query):
    filename = query + "Dump.txt"
    #Search wikipedia for data
    print("Getting data...")
    data = pullData(query)
    #Write to file
    if(data != "dead"):
        print("Writing to file " + str(filename) + "...")
        writer(filename, data)
        #Clean up directory
        print("Moved files into dumpfile directory")
        relocate(filename) #--opting to use Makefile do this instead
        print("Completed")
    else:
        print("query no good")

def usage():
    print("python3 GetData.py <query|file-of-queries>")

#Driver
def main():
    #Get query && set filename
    query = getQuery()
    help = (query == "--help" or query == "-help" or query == "-h") # boolean
    if(help == True):
        usage()
    if(help == False):
        if(query == "-auto"):
            query = read()
            size = len(query)
            for i in range(size):
                execute(query[i])
        else:
            execute(query)

#The big red button
main()