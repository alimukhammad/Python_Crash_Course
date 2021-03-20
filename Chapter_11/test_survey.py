import unittest
from survey import AnonemousSurvay

class TestAnonemousSurvay(unittest.TestCase):
    # Test for the class AnonemousSurvay

    def setUp(self):
    #     Create a survey and a set of responses for use in all test methods
        question = "What language did you first learn to speak?"
        self.my_survey = AnonemousSurvay(question)
        self.responses = ['Englsh', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        # Test that a single response is tored properly
        # my_survey.store_response("English")
        self.my_survey.store_response(self.response[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
#         Test that three individual responses are stored propelry
#         question = "What language did yo ulearn to speak?"
#         my_survey = AnonemousSurvay(question)
#         responses = ["English", "Spanish", "Mandarin"]
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()