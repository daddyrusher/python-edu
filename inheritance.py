class Student(object):
    def __init__(self):
        super(Student, self).__init__()
        pass

    def message(self):
        print('I have finally graduated')


class Graduate(Student):
    def __init__(self):
        super(Graduate, self).__init__()
        pass

    def message(self):
        print('I will now do my masters!')
        super(Graduate, self).message()


class Master(Graduate):
    def __init__(self):
        super(Master, self).__init__()
        pass

    def message(self):
        print('')


class Grandmaster(Master):
    def __init__(self):
        super(Grandmaster, self).__init__()
