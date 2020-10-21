import mongoengine as me
me.connect('testtetsttetst')


class Task(me.Document):
    LOW_PRIORITY = 1
    MEDIUM_PRIORITY = 2
    HIGH_PRIORITY = 3

    PRIORITIES = (
        (LOW_PRIORITY, 'Низкий приоритет'),
        (MEDIUM_PRIORITY, 'Средний приоритет'),
        (HIGH_PRIORITY, 'Высокий приоритет')
    )

    INSIDE_CATEGORY = 1
    OUTSIDE_CATEGORY = 2

    CATEGORIES = (
        (INSIDE_CATEGORY, 'Проблема в магазине'),
        (OUTSIDE_CATEGORY, 'Проблема на складе'),
    )
    priority = me.IntField(choices=PRIORITIES)
    category = me.IntField(choices=CATEGORIES)