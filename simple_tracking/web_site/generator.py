from simple_tracking.utils.singleton import Singleton


class IdGenerator(metaclass=Singleton):
    # todo: persist last id

    def __init__(self):
        self.__current_id = 0

    def next(self):
        self.__current_id += 1
        return self.__current_id
