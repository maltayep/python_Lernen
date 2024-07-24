#print("Practice writing some expressions and conversions yourself.
#In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. 
#Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files 
#variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. 
#Remember to use the  function to convert the number into a string")
# List of file sizes
file_sizes = [2048, 4357, 97658, 125, 8]

# Calculate the sum of the file sizes
total_size = sum(file_sizes)

# Manually set the files variable to the number of files
files = 2

# Calculate the average file size
average_size = total_size / files

# Output the result
print("The average size is: " + str(average_size))
