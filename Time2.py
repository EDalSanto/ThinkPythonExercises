class Time(object):
    """Represents the time of day.

    attributes: s, seconds from midnight
    """
    def __init__(self, s=0):
        self.s = s

    def __str__(self):
        return '%d' % (self.s)

    def print_time(self):
        print str(self)

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.s

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.s > other.s

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print 'Is end after start?',
    print end.is_after(start)

    print 'Using __str__'
    print start, end

    start = Time(9, 45)
    duration = Time(1, 35)
    print start + duration
    print start + 1337
    print 1337 + start

    print 'Example of polymorphism'
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print total


if __name__ == '__main__':
    main()
