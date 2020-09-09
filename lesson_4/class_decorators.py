class Triangle1:

    type_ = 'triagnle'
    description = 'This class implements logic for triangle figure'

    def get_type(self):
        return self.type_

    # @staticmethod
    # def get_class_info():
    #     return Figure.type_, Figure.description

    @classmethod
    def get_class_info_2(cls):
        return cls.type_, cls.description




print(Triangle1.get_class_info_2())