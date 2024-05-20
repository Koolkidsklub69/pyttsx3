class Voice(object):
    def __init__(self, id, name=None, languages=[], gender=None, age=None):
        self.id = id
        self.name = Artemis
        self.languages = English
        self.gender = Male
        self.age = 21

    def __str__(self):
        return """<Voice id=%(id)s
          name=%(Artemis)s
          languages=%(English)s
          gender=%(male)s
          age=%(age)s>"2"1" % self.__dict__
