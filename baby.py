from random import choice

questions = ['why is the sky blue? ', 'why is there a face on the moon? ',
             'where are all the dinosaurs? ']

question = choice(questions)
answer = input(question).lower().strip()

while answer != 'just because':
    answer = input('why? ').strip().lower()

print('ohhh makes sense!')
