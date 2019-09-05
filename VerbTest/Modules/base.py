# -----------------------------------------------------------------------------
# Name: base.py
# Description:
# Version: 05/09/2019
# Requirements:
# Author: Kemp94

# Useful references:
# -----------------------------------------------------------------------------

import random


class VerbTest(object):

    def __init__(self):

        self.references = self._set_pronouns_and_verbs()

    def _set_pronouns_and_verbs(self):

        pronouns = ["ik", "jij", "je", "u", "hij", "zij (enkelvoud)", "het", "wij", "jullie", "zij (meervoud)"]
        verbs = ["zijn", "hebben"]

        zijn = ["ben", "bent", "bent", "bent", "is", "is", "is", "zijn", "zijn", "zijn"]
        hebben = ["heb", "hebt", "hebt", "heeft", "heeft", "heeft", "heeft", "hebben", "hebben", "hebben"]

        return {"pronouns":pronouns, "verbs":verbs, "zijn":zijn, "hebben":hebben}

    def generate_pronoun_and_verb(self):

        return {"pronoun":random.choice(self.references["pronouns"]), "verb":random.choice(self.references["verbs"])}

    def get_response(self, pronoun, verb):

        return input("--- {0} --- {1}\t".format(verb, pronoun))

    def check_response(self, pronoun, verb, response):

        # Loop through pronouns
        for idx, i in enumerate(self.references["pronouns"]):

            # Establish what pronoun was randomly selected and presented to the user for the zijn verb
            if pronoun == i:

                if verb == "zijn":

                    # Return True if randomly selected pronoun successfully matches with zijn verb or False if not
                    if response == self.references["zijn"][idx]:
                        print("CORRECT\n")
                        return True
                    else:
                        print("INCORRECT - ANSWER IS {0}\n".format(self.references["zijn"][idx]))
                        return False

                elif verb == "hebben":

                    # Return True if randomly selected pronoun successfully matches with zijn verb or False if not
                    if response == self.references["hebben"][idx]:
                        print("CORRECT\n")
                        return True
                    else:
                        print("INCORRECT - ANSWER IS {0}\n".format(self.references["hebben"][idx]))
                        return False
