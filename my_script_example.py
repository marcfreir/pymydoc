class Greeter:
    """
    A class to represent a greeter.
    """

    def __init__(self, name):
        """
        Initialize the greeter with a name.
        
        Args:
            name (str): The name of the person.
        """
        self.name = name

    def greet(self):
        """
        Returns a greeting message.
        
        Returns:
            str: A greeting message.
        """
        return f"Hello, {self.name}!"
