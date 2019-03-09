#global variable
f = "sample.txt"
words_to_skip = ["a", "the", "is", "for", "and"]
head_words = ["head", "eye", "eyes", "ear", "ears", "cheek", "cheeks",
              "forehead", "temple", "temples", "mouth", "tooth", "teeth"
              "tongue", "lips"]
upper_body_words = ["neck", "throat", "shoulder", "shoulders", "arm", "arms",
                    "bicep", "biceps", "tricep", "triceps", "forearm", "forearms",
                    "hand", "hands", "finger", "fingers", "chest", "breast", "heart",
                    "back", "stomach"]
lower_body_words = ["leg", "legs", "thigh", "hamstring", "hamstrings", "buttocks", "hip",
                    "hips", "knee", "knees", "foot", "feet", "toe", "toes"]
general_wounds = ["cut", "cuts", "bruise", "bruises", "sore", "sores", "ache", "aches", "hurt", "hurts", "hurting",
                  "itch", "itches", "itching", "blood", "bleed", "bleeding", "red", "broken"]

body_list = []
wound_list = []
#USER
class Person:
    def __init__(self, name, age, symptom_list):
        self.name = name
        self.age = age
        self.symptom_list = symptom_list


class SymptomList:
    def __init__(self, body_parts, severity):
        self.body_parts = body_parts
        self.severity = severity



#gets parsed input and sets the data to a person
def generate_symptom_list(filename):
    f = open(filename, "r")
    lines = f.readlines()

    for i in lines:
        curr_line = i.split(" ")
        #curr_line is an array of words
        parse_keywords(curr_line)

#goes through each word
def parse_keywords(current_line):
    for i in current_line:
        val = skip_words(i)
        #if it a word to skip, increment i
        if val == 1:
            continue
        check_general_wounds(i)
        check_head(i)
        check_upper_body(i)
        check_lower_body(i)

def output_suggestions(person):
    print("Hello, " + person.name + ".")
    i = validate_symptoms()
    if (i == 1):
        return
    else:
        print("From what we understand, these are your symptoms: ")
        assess_symptoms()
        print("Here are some possible reasons for your conditions: ")
        print("We suggest you consider the following solutions: ")

#prints keywords
def print_symptoms(symptom_list):
    for i in symptom_list:
        print(i)

#checks if the word is in words_to_skip, return 1 = skip, return 0 = don't skip
def skip_words(word):
    for i in words_to_skip:
        if word == i:
            return 1
    return 0

#check if the word is related to a general wound
def check_general_wounds(word):
    for i in general_wounds:
        if i == word:
            wound_list.append(i)

#check if the word is related to the head
def check_head(word):
    for i in head_words:
        if i == word:
            body_list.append(i)

#check if the word is related to the upper body
def check_upper_body(word):
    for i in upper_body_words:
        if i == word:
            body_list.append(i)

#check if the word is related to the lower body
def check_lower_body(word):
    for i in lower_body_words:
        if i == word:
            body_list.append(i)


#output understood symptoms
def assess_symptoms():
    max_len = len(wound_list)
    if (len(body_list) > max_len):
        max_len = len(wound_list)
    for i in range(0,max_len):
        print("Your " + body_list.index(i) + " is " + wound_list.index(i))
        





#output possible reasons for symptoms
#def assess_possibilities():


#output suggested solutions
#def assess_solutions():


#symptoms not specific enough
def validate_symptoms():
    if (len(wound_list) < 1 or len(body_list) < 1):
        print("Please provide more information so we may better assist your needs.")
        return 1    #fail
    else:
        return 0    #pass


def main():
    person1 = Person("Bob", 12, generate_symptom_list(f))
    print_symptoms(body_list)
    output_suggestions(person1)


main()


