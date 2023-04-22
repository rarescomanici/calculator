try:
    import tkinter
except ImportError:     # python 2
    import Tkinter as tkinter


def add(entry_box):
    """
    Stores the first term and adds the next number inputted
    :param entry_box: entry box
    :return:
    """
    global first_term, operation
    first_term = int(entry_box.get())
    operation = "+"
    entry_box.delete(0, "end")


def subtract(entry_box):
    """
    Stores the first term and subtracts the next number inputted
    :param entry_box: entry box
    :return:
    """
    global first_term, operation
    first_term = int(entry_box.get())
    operation = "-"
    entry_box.delete(0, "end")


def multiply(entry_box):
    """
    Stores the first term and multiplies by the next number inputted
    :param entry_box: entry box
    :return:
    """
    global first_term, operation
    first_term = int(entry_box.get())
    operation = "*"
    entry_box.delete(0, "end")


def divide(entry_box):
    """
    Stores the first term and divides by the next number inputted
    :param entry_box: entry box
    :return:
    """
    global first_term, operation
    first_term = int(entry_box.get())
    operation = "/"
    entry_box.delete(0, "end")


def global_clear(entry_box):
    """
    Deletes current entry and result
    :param entry_box: entry to be cleared
    :return:
    """
    global final_result, first_term, operation
    final_result = 0
    first_term = 0
    operation = ""
    entry_box.delete(0, "end")


def local_clear(entry_box):
    """
    Deletes current entry
    :param entry_box: entry to be cleared
    :return:
    """
    entry_box.delete(0, "end")


def equals(entry_box):
    """
    Updates entry by showing the result of the operation
    :param entry_box: entry to be updated
    :return:
    """
    global first_term, operation, final_result
    if operation == "+":
        final_result = first_term + int(entry_box.get())
        first_term = final_result
    if operation == "-":
        final_result = first_term - int(entry_box.get())
        first_term = final_result
    if operation == "*":
        final_result = first_term * int(entry_box.get())
        first_term = final_result
    if operation == "/":
        try:
            final_result = first_term / int(entry_box.get())
            first_term = final_result
        except ZeroDivisionError:
            final_result = "undefined"
            first_term = 0
    entry_box.delete(0, "end")
    entry_box.insert(0, final_result)


def number_insert(entry_box, number):
    entry_box.insert("end", number)


