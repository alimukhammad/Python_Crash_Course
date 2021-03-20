from survey import AnonemousSurvay

#  Define a question and make a survey
question = "what language did you first learn to speak?"
my_survey = AnonemousSurvay(question)

# show the question and store responses to the qustion
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey")
my_survey.show_results()