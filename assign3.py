"""
Bradley Kimutai Kosgei
CS51A
Assignment 3
02/07/2022
"""

from assign3_quotes import *
from random import randint
# ----------------------------------------------------------------------------------------------------------------------
# Movie Quotes Analysis Question


def is_question(statement):
    """
    Determines whether the string given ends in a question mark or not
    :param statement: (str) any string
    :return: (bool) whether the statement is a question or not
    """
    if statement[-1] == "?":  # the position -1 is the last position on the string
        return True
    else:
        return False


def get_first_quotes(quotes):
    """
    Picks out the first quotes in the list of tuples
    :param quotes: (list) the list of tuples
    :return: (list) the list of first items in the tuples
    """
    list_1 = []  # we first input a blank list

    for first_item, second_item in quotes:
        list_1.append(first_item)  # adds the first items only into the blank list
    return list_1


def get_first_questions(questions):
    """
    Finds the first quotes that are questions only
    :param questions: (list) the list of tuples
    :return: (list) the first items in the tuples that are questions
    """
    list_2 = []

    first_quotes = get_first_quotes(questions)  # we use first items we found earlier

    for item in first_quotes:
        if is_question(item):  # only first items that are questions will be chosen
            list_2.append(item)  # we add the first items questions to the empty list
    return list_2


def count_question_quotes(data):
    """
    Counts the number of first items that are question
    :param data: (list) the list of tuples
    :return: (int) the number of first items that are questions
    """
    first_questions = get_first_questions(data)  # calls the function that gives first questions only
    return len(first_questions)
# There are 71117 first quotes in the real data that are questions


def get_average_question_length(data):
    """
    Gives the average length of all first quotes that are questions
    :param data: (list) the list of tuples
    :return: (float) the average length
    """
    first_questions_2 = get_first_questions(data)
    total = 0

    for item in first_questions_2:
        total = total + len(item)  # counts the specific amount of characters in the questions

    number = count_question_quotes(data)

    return total / number  # returns the average length as a floating point


# ----------------------------------------------------------------------------------------------------------------------
# Chatbot Section


def get_responses(quotes, question):
    """
    Provides the corresponding response to each first item input as parameter
    :param quotes: (list) our list of tuples
    :param question: (str) the first item in our list of tuples
    :return: (str) gives the response to the first item
    """
    list_3 = []

    for first_item, second_item in quotes:
        if question == first_item:  # uses conditionals to provide the response required
            list_3.append(second_item)  # adds the responses into the empty list
    return list_3


def get_random_from_list(numbers):
    """
    Randomly gives one of the parts of the list input
    :param numbers: (list) any list input
    :return: a randomly chosen index of the stated list
    """
    random = randint(0, len(numbers)-1)  # chooses a random index from index 0 to the last which is n-1
    return numbers[random]


def respond(quotes, question):
    """

    :param quotes: (list) our list of tuples
    :param question: (str) the first item in our list of tuples
    :return: a randomly chosen response to the question if there are multiple first questions and "I don't know"
    if the question does not exist on our list
    """
    second = get_responses(quotes, question)

    if len(second) == 0:  # if the list is empty then the quote does not exist on our list
        return "I don't know."
    else:
        return get_random_from_list(second)  # randomizes the response if there is more than one first quote


def chatbot():
    """
    This is a chatbot that accepts string input from a user and continues the conversation by giving responses from
    data from certain movie quotes and ends when it gets the input "bye".
    :return: combines some of our previous functions to give the chatbot itself
    """
    print("Welcome! \nAsk me anything. When you’re done, just type ’bye’")
    chat = input("-").lower()

    quotes = get_quotes()

    while chat != "bye":  # while loop keeps asking for input till "bye" is input
        if not is_question(chat):  # prints out if the string is not a question
            print("I only respond to questions!")
        else:
            print(respond(quotes, chat))  # randomizes the response if the input is in the movie quotes and says
            # I don't know if it is not present

        chat = input("-").lower()  # prevents the code from going on and on









































