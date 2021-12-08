"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Make a new generator, starting at start."""
        self.next = start
        self.start = start
    
    def generate(self):
        """Return next serial."""
        self.next = self.next + 1
        return self.next - 1

    def reset(self):
        """Reset number to original start."""
        self.next = self.start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"
