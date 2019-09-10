# -----------------------------------------------------------------------------
# Name: main.py
# Description:
# Version: 05/09/2019
# Requirements:
# Author: Kemp94

# Useful references:
# -----------------------------------------------------------------------------

import collections
from .Modules import VerbTest


class VerbTestRunner(VerbTest):

    def __init__(self):

        print("\n-----***** LET'S PLAY THE VERB GAAAAAAMMMEEEEEEEEE!!!! *****-----\n")

        super().__init__()

    def runner(self, test_length):

        results_list = []
        for num in range(test_length):

            pronoun_and_verb = self.generate_pronoun_and_verb()

            response = self.get_response(pronoun_and_verb["pronoun"], pronoun_and_verb["verb"])

            response_check = self.check_response(pronoun_and_verb["pronoun"], pronoun_and_verb["verb"], response)

            results_list.append(response_check)

        score = collections.Counter(results_list)
        print("\n-----***** END OF TEST!!!! *****-----\nSCORE: {0}/{1}".format(score[True], len(results_list)))


if __name__ == "__main__":

    vtr = VerbTestRunner()

    vtr.runner(10)
