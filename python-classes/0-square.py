    """
        Why size is private attribute?
        The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
    """

class Square:
    def __init__(self, size):
        self.__size = size