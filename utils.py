from enum import IntEnum, unique

@unique
class Mode(IntEnum):
    CLIENT_TO_SERVER = 0
    SERVER_TO_CLIENT = 1