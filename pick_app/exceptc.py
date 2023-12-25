class NullExcept(Exception):
    def __init__(self):
        self.message = "Значение меньше 1"

    def __str__(self):
        return self.message


class InvalidSettingsException(Exception):
    def __init__(self):
        self.message = f"Invalid settings value"

    def __str__(self):
        return self.message


class GetData(Exception):
    def __init__(self):
        self.message = "Invalid record format"

    def __str__(self):
        return self.message


class RecordIdTypeException(Exception):
    def __init__(self):
        self.message = "An ID must be of numeric type"

    def __str__(self):
        return self.message


class PictureClassInitError(Exception):
    def __init__(self):
        self.message = "Both URL and title must be of string type"

    def __str__(self):
        return self.message
