from flask import jsonify
from controller import check_field

def field_translation(obj):
    translator = {
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'E': '5',
        'F': '6',
        'G': '7',
        'H': '8'
    }

    obj.field = translator[obj.field[0]] + obj.field[1]


class Figure:
    def __init__(self, field: str, colour: str):
        self.field = field
        self.colour = colour
        self.name = self.__class__.__name__.lower()
        field_translation(self)

    def list_available_moves(self):
        pass

    def validate_moves(self, moves_list):

        result = []

        for i in moves_list:
            if int(i.field[0]) > 8 or int(i.field[1]) > 8:
                continue
            elif check_field(self.field):
                continue
            else:
                result.append(i)
        return result





class Pawn(Figure):
    def list_available_moves(self):
        result = []

        if self.field[1] == 2 and self.colour == 'W':
            result.append(self.field[0] + str(int(self.field) + 2))

        elif self.field[1] == 7 and self.colour == 'B':
            result.append(self.field[0] + str(int(self.field) - 2))

        elif self.colour == 'B':
            result.append(self.field[0] + str(int(self.field) - 1))

        else:
            result.append(self.field[0] + str(int(self.field) + 1))

        return self.validate_moves(result)



class Knight(Figure):
    pass


class Bishop(Figure):
    pass


class Rook(Figure):
    pass


class Queen(Figure):
    pass


class King(Figure):
    pass


if __name__ == '__main__':
