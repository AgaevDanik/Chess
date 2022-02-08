from sqlalchemy import select, insert, delete, update

from database import engine, figures


def field_detranslation(obj):
    translator = {
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H',
    }

    obj.field = translator[obj.field[0]] + obj.field[1]

    return obj


def select_figure_by_field(field):
    with engine.connect() as connection:
        query = select([figures]).where(figures.c.field == field)
        result = connection.execute(query)
        return result


def update_figure_by_field(current_field, destination_field):
    with engine.connect() as connection:
        pass


def delete_all():
    with engine.connect() as connection:
        query = delete(figures)
        connection.execute(query)


def insert_figure(figure):
    figure = field_detranslation(figure)
    with engine.connect() as connection:
        query = insert(figures).values(name=figure.name,
                                       field=figure.field,
                                       colour=figure.colour, )
        connection.execute(query)


def check_field(field):
    with engine.connect() as connection:
        query = select([figures]).where(figures.c.field == field)
        result = connection.execute(query)
        for i in result:
            result = i.field
        if result == field:
            return False
        else:
            return True
