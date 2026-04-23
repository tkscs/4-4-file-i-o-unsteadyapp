# Read and print the contents of the file "q1.txt"
text = open("q1.txt","r")
print(text.read())
text.close()
#or 
with open("q1.txt","r") as f:
    print(f.read())
