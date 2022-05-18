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


def count_questions_quotes(data):
    """
   Counts the number of first items that are questions
   :param data: (list) the list of tuples
   :return: (int) the number of first items that are questions
   """

    first_questions = get_first_questions(data)
    return len(first_questions)
# There are 71117 first quotes in the real data that are questions


def get_average_question_length(data):
    """

    :param data:
    :return:
    """
    first_questions_2 = get_first_questions(data)
    total = 0

    for item in first_questions_2:
        total = total + len(item)

    number = count_questions_quotes(data)

    return total / number


# ----------------------------------------------------------------------------------------------------------------------
# Chatbot Section


def get_responses(quotes, question):
    """

    :param quotes:
    :param question:
    :return:
    """
    list_3 = []

    for first_item, second_item in quotes:
        if question == first_item:
            list_3.append(second_item)
    return list_3


def get_random_from_list(numbers):
    """

    :param numbers:
    :return:
    """
    random = numbers[randint(0, len(numbers))]
    return random


def respond(quotes, question):
    """

    :param quotes:
    :param question:
    :return:
    """
    second = get_responses(quotes, question)
    random_second = get_random_from_list(second)

    if len(second) == 0:
        return "I don't know."
    else:
        return random_second






































