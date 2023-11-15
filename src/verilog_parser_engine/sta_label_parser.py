import sys
import os
import re
import json


# Dynamically determine the path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)


def read_tempus_log(tempus_log_file_directory):
    # Check if the file exists
    if not os.path.isfile(tempus_log_file_directory):
        raise FileNotFoundError(f"The file '{tempus_log_file_directory}' does not exist.")

    # Read the file
    with open(tempus_log_file_directory, 'r') as file:
        content = file.read()
        return content


def sta_label_parser(tempus_log_file_directory):

    content = read_tempus_log(tempus_log_file_directory)



