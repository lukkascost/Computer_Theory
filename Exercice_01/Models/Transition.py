class Transition:
    def __init__(self, start, end, receive):
        self.start = start
        self.end = end
        self.received = receive

    def __eq__(self, other):
        return "S({},{})".format(self.start.name, self.received) == other

    def __str__(self):
        return '\tS({},{}) => {}'.format(self.start.name, self.received, self.end.name)
