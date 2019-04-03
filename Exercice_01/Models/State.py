class State(object):
    def __init__(self, state_name, is_initial=False, is_end=False):
        self.name = state_name
        self.is_initial = is_initial
        self.is_end = is_end

    def __eq__(self, other):
        return self.name == other

    def __str__(self):
        return "\tState: {}".format(self.name)
