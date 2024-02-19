class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, num):
        self.total_strength += num

    def dropStudents(self, num):
        self.total_strength -= num

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name
