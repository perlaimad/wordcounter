file_path = r'C:\Users\User\OneDrive\Desktop\wordcounter\lamb girl.txt'  

try:
    file = open(file_path, 'r')
    word_count = 0
    for line in file:
        # Split the line into words and count them
        words = line.split()
        word_count += len(words)
    file.close()
    print("Number of words in file:", word_count)

except FileNotFoundError:
    print("File not found. Please check the path and try again.")
