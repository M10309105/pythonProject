#/usr/bin/python3
#
#Exception
print("=" * 100)
print("8.6 Custom Exception Class")
print("=" * 100)

#user defined exception clss need extend base exception class

class Error(Exception):
    pass


class MyError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self,message,expression):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

#exception class use Error in end