###this program computes the complementary DNA bases to any given 5' to 3' sequence in 5' to 3' direction
print('''Enter 1 if your sequence is in 5' to 3' direction.
Enter 2 if your sequence is in 3' to 5' direction.''' )
while True:
    dna_direction = input('>')
    #if invalid sequence is entered, it asks for user input again
    if dna_direction not in ['1', '1.','2','2.']:
        print('Please enter 1 or 2.')
    else:
        break
print('Enter your DNA sequence.')

sequence = input('>')
#defining what will be printed
complementary_sequence = ''
#here is the loop that analyzes each character in the inputted sequence
for char in sequence:
    if char == 'A':
        complementary_sequence += 'T'
    elif char == 'T':
        complementary_sequence += 'A'
    elif char == 'C':
        complementary_sequence += 'G'
    elif char == 'G':
        complementary_sequence += 'C'
#this will reverse the complementary strand (which was given in 5' to 3' direciton) so that the output in 5' to 3' direction
if dna_direction in ['1', '1.']:
    ordered_complementary_sequence = complementary_sequence[::-1]
    print("5' " + ordered_complementary_sequence + " 3'")
#no need to reverse the sequence if the input is in 3' to 5' direction
else:
    print("5' " + complementary_sequence + " 3'")



