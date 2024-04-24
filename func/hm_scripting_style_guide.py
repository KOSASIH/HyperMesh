#!/usr/bin/env python3

"""
File      : hm_scripting_style_guide.py
Date      : April 24, 2024
Created by: Your Name
Purpose   : Provide a style guide for HyperMesh scripting.
"""

import os
import sys
import time
import random

# Initialize variables
my_var = 10

# Define a procedure
def my_proc(arg1, arg2):
    """
    Purpose:  Perform a specific task.
    Args:
        - arg1: The first argument.
        - arg2: The second argument.
    Returns:
        The result of the task.
    Notes:
        - Any special information, assumptions, or warnings.
    """
    # Initialize variables
    result = 0

    # Perform the task
    result = arg1 + arg2

    # Return the result
    return result

# Define a namespace
namespace my_namespace {
    variable my_namespace_var 20

    proc my_namespace_proc {arg1} {
        # Initialize variables
        result 0

        # Perform the task
        result [expr {$arg1 * 2}]

        # Return the result
        return $result
    }
}

# Use the procedure and namespace
print(my_proc(my_var, my_namespace::my_namespace_var))

# Define a class
class MyClass:
    """
    Purpose:  Represent a specific object.
    Args:
        - arg1: The first argument.
        - arg2: The second argument.
    Returns:
        A new instance of MyClass.
    Notes:
        - Any special information, assumptions, or warnings.
    """

    # Initialize the class
    def __init__(self, arg1, arg2):
        # Initialize variables
        self.var1 = arg1
        self.var2 = arg2

    # Define a method
    def my_method(self):
        """
        Purpose:  Perform a specific task.
        Args:
            None.
        Returns:
            The result of the task.
        Notes:
            - Any special information, assumptions, or warnings.
        """
        # Initialize variables
        result = 0

        # Perform the task
        result = self.var1 + self.var2

        # Return the result
        return result

# Use the class
my_obj = MyClass(my_var, my_namespace::my_namespace_var)
print(my_obj.my_method())
