import re
import random


class RuleBot:
    # Potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # Exit Conversation
    exit_conversation = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # Random starter question
    randon_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Does earth have a leader?",
        "Is there intelligent life on this planet?",
        "What planets have you visited?",
        "What technology do you have on this planet?",
    )

    def __init__(self):
        self.allienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                             'answer_why_intent': r'why\sare.*',
                             'about_intellipat': r'.*\s*intellipat'
                             }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am Rule-Bot. Will you help me to learn about your planet?\n")
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay,have a nice earth day")
                return True

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipat':
                return self.about_intellipat()
        if not found_match:
            return self.no_match_intent()

    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and specifies.\n",
                     "I am from Opidipus, the capital of the Wayward Galaxies.\n")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("I come in peace \n", "I am here to collect data on your planet and its inhabitants\n",
                     "I heard the coffee is good\n")
        return random.choice(responses)

    def about_intellipat(self):
        responses = ("Intellipat is the world largest professional educational company.\n",
                     "Intellipat will make you learn concepts in the easy way.\n", "Intellipat is where your career and skills grows.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Please tell me more.\n", "Tell me more.\n",
                     "I need more details\n", "The given details do not matches.\n")
        return random.choice(responses)


AlienBot = RuleBot()
AlienBot.greet()
