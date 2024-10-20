import os
import re
from collections import Counter
import socket

# Define file paths
input_dir = '/home/data'
output_file = os.path.join(input_dir, 'output', 'result.txt')

# Helper function to read files
def read_file(file_name):
    with open(os.path.join(input_dir, file_name), 'r') as file:
        return file.read().lower()

# Split contractions into separate words
def handle_contractions(text):
    text = re.sub(r"(?i)\b(can't|won't|don't|i'm|you're)\b", lambda x: {
        "can't": "can not", "won't": "will not", "don't": "do not",
        "i'm": "i am", "you're": "you are"
    }[x.group().lower()], text)
    return re.findall(r'\w+', text)

# Read and process both files
text_if = read_file('IF.txt')
text_arutw = read_file('AlwaysRememberUsThisWay.txt')

# Count words in each file
words_if = re.findall(r'\w+', text_if)
words_arutw = handle_contractions(text_arutw)

# Count the total number of words
total_words_if = len(words_if)
total_words_arutw = len(words_arutw)
grand_total_words = total_words_if + total_words_arutw

# Find the top 3 most frequent words
top_words_if = Counter(words_if).most_common(3)
top_words_arutw = Counter(words_arutw).most_common(3)

# Get IP address of the machine running the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to result.txt
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as result:
    result.write(f"Total words in IF.txt: {total_words_if}\n")
    result.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_arutw}\n")
    result.write(f"Grand total words: {grand_total_words}\n\n")
    result.write(f"Top 3 most frequent words in IF.txt:\n")
    for word, count in top_words_if:
        result.write(f"{word}: {count}\n")
    result.write(f"\nTop 3 most frequent words in AlwaysRememberUsThisWay.txt (with contractions handled):\n")
    for word, count in top_words_arutw:
        result.write(f"{word}: {count}\n")
    result.write(f"\nIP Address of the container: {ip_address}\n")

# Print the result to console
with open(output_file, 'r') as result:
    print(result.read())
