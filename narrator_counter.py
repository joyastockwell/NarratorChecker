# creating variable to store the
# number of words the narrator says
total_narrator_words = 0

# returns length of line if line does not contain
# a colon. if it contains a colon, it must not be
# a narrator line, so returns zero for lines containing
# a colon
def get_words_narrator_says(curr_line):
    line_narrator_words = 0
    index = curr_line.find(":")
    if index == -1:
        # print(curr_line)
        line_narrator_words = len(curr_line.split())
        #print(line_narrator_words)
    return line_narrator_words
    
 
# Opening our text file in read only
# mode using the open() function
with open(r'C:\Users\stockwja\Downloads\Porfiro.docx.txt', 'r', encoding="utf8") as file:

#with open(r'C:\Users\stockwja\Downloads\test.txt', 'r') as file:
 
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
 
    # Splitting the data into separate lines
    # using the splitlines() function
    lines = data.splitlines()

#    print(lines)
    # Iterating over every line from the data
    for curr_line in lines:
        total_narrator_words += get_words_narrator_says(curr_line)
 
# Printing total number of words
print(total_narrator_words)