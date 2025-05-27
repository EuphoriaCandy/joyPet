# class that creates and sets up a new joyPet

import os
import sys

class joyPetCreator:
  def __init__(self):
    self.firstPet_bool = None
    self.petName = ''
    self.ownerName = ''

  def askQuestion(self, question_text, acceptable_answers, custom_invalid_msg=None, scrub_input=False):
    '''
    Function for presenting input prompt question to user, repeats loop if answer is not acceptable. 
    '''
    question_input_invalid = True # defaults to true
    invalid_msg = 'Answer not understood. Acceptable answers are: \n {}'.format(', '.join(acceptable_answers)) #default

    if custom_invalid_msg is not None:
      invalid_msg = custom_invalid_msg
    
    while question_input_invalid: # break loop and continue when valid input received
      question_input = input(question_text)

      if scrub_input: # (optional) scrub user question input to make parsing easier
        question_input = question_input.strip().lower() # scrub answer to make parsing easier

      if question_input in acceptable_answers:
        question_input_invalid = False # break loop
        return question_input
      else:
        print(invalid_msg)

  def createJoyPet(self):
    print('Hello! Welcome to the wonderful world of joyPets! Let\'s create a new joyPet!')


question_input = input('Have you created a joyPet before? (y/n)')

#if first_pet_ans.lower() == 'y'


#os.makedirs('new_directory_name', exist_ok=True)