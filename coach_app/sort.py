__author__ = 'gregorylevin'

# see
# https://wiki.python.org/moin/HowTo/Sorting
# http://www.pythonlearn.com/html-008/cfbook011.html

from operator import itemgetter, attrgetter
from pprint import pprint

# for sorting a dictionary:
#     http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python


def print_coach():

  coach_dict = {
        "john doe":     ["31 scott st", "INTP"],
        "jane lee":     ["20 roosevelt st", "EZTJ"],
        "zack tod":     ["45 bell st", "ESFP"],
        "igor t":       ["45 bell st", "ENFP"],
        "matt beelt":   ["21 crystal st", "ENTJ"],
  }

    # coach_tuples = [
    #     ('john doe', '31 scott st', 'INTP'),
    #     ('jane lee', '20 roosevelt st', 'EZTJ'),
    #     ('zack tod', '45 bell st', 'ESFP'),
    #     ('igor t', '45 bell st', 'ENFP'),
    #     ('matt beelt', '21 crystal st', 'ENTJ'),
    #     ]


    # list = []
    # for i in coach_tuples:
    #     list.append(i)

  #
  # coaches = {'coach_dict', coach_dict}
    # string = str(sorted(coach_tuples))

  names = coach_dict.keys()
  locations = coach_dict.values()

  # list = []
  # for k, v in coach_dict.items():
  #     list.append(k), list.append(v)

  print names, locations
  return names, locations


print_coach()








