'''
A Lunar Calendar for Python

Support Korean, Chinese with Lunar Table
'''


import datetime

class LunarDateBaseError(Exception):
    """The base class for other LunarDate exceptions"""

    def __init__(self, value):
        super(LunarDateBaseError, self).__init__(value)
        self.value = value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return ("<LunarDateBaseError in " + repr(self.value) + ">")


class InvalidInputRangeError(LunarDateBaseError):
    """The InvalidInputRangeError class for other LunarDate exceptions"""

    def __init__(self, value):
        super(InvalidInputRangeError, self).__init__(value)
        self.value = value

    def __repr__(self):
        return ("<InvalidInputRangeError in " + repr(self.value) + ">")


KOREAN_LUNAR_YEAR_INFO = [
        [384, 1, 2, 1, 1, 2, 1, 2, 4, 2, 2, 1, 2],
        [354, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1],
        [355, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2],
        [383, 1, 2, 1, 2, 3, 2, 1, 1, 2, 2, 1, 2],
        [354, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1],
        [355, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2],
        [384, 1, 2, 2, 5, 1, 2, 1, 2, 1, 2, 1, 2],
        [354, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1],
        [355, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2],
        [384, 1, 4, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2],
        [354, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1],
        [384, 2, 1, 2, 1, 1, 4, 1, 2, 2, 1, 2, 2],
        [354, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2],
        [354, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2],
        [384, 2, 2, 1, 2, 4, 1, 2, 1, 2, 1, 1, 2],
        [355, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        [354, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1],
        [384, 2, 3, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1],
        [355, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2],
        [384, 1, 2, 1, 1, 2, 1, 4, 2, 2, 1, 2, 2],
        [354, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2],
        [354, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2],
        [384, 2, 1, 2, 2, 3, 2, 1, 1, 2, 1, 2, 2],
        [354, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2],
        [354, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1],
        [385, 2, 1, 2, 4, 2, 1, 2, 2, 1, 2, 1, 2],
        [354, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1],
        [355, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2],
        [384, 1, 4, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2],
        [354, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2],
        [383, 1, 2, 2, 1, 1, 4, 1, 2, 1, 2, 2, 1],
        [354, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1],
        [355, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2],
        [384, 1, 2, 2, 1, 6, 1, 2, 1, 2, 1, 1, 2],
        [355, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2],
        [354, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1],
        [384, 2, 1, 5, 1, 2, 1, 2, 1, 2, 2, 2, 1],
        [354, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1],
        [384, 2, 2, 1, 1, 2, 1, 5, 1, 2, 2, 1, 2],
        [354, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2],
        [354, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
        [384, 2, 2, 1, 2, 2, 5, 1, 1, 2, 1, 2, 1],
        [355, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2],
        [355, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2],
        [384, 1, 1, 2, 5, 1, 2, 1, 2, 2, 1, 2, 2],
        [354, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2],
        [354, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2],
        [384, 2, 4, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2],
        [354, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2],
        [384, 2, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2],
        [354, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1],
        [355, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        [384, 1, 2, 1, 2, 5, 2, 1, 2, 1, 2, 1, 2],
        [355, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2],
        [354, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2],
        [384, 2, 1, 5, 1, 1, 2, 1, 2, 1, 2, 2, 2],
        [354, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2],
        [384, 2, 1, 2, 1, 2, 1, 1, 4, 2, 1, 2, 2],
        [354, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2],
        [354, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [384, 2, 1, 2, 1, 2, 4, 2, 1, 2, 1, 2, 1],
        [355, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2],
        [354, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1],
        [384, 2, 1, 2, 3, 2, 1, 2, 1, 2, 2, 2, 1],
        [355, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2],
        [354, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2],
        [383, 1, 2, 4, 2, 1, 1, 2, 1, 1, 2, 2, 1],
        [355, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2],
        [384, 1, 2, 2, 1, 2, 1, 4, 2, 1, 2, 1, 2],
        [354, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1],
        [355, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2],
        [384, 1, 2, 1, 1, 4, 2, 1, 2, 2, 2, 1, 2],
        [354, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1],
        [354, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1],
        [384, 2, 2, 1, 4, 1, 2, 1, 1, 2, 2, 1, 2],
        [354, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2],
        [384, 2, 2, 1, 2, 1, 2, 1, 4, 2, 1, 1, 2],
        [354, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1],
        [355, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1],
        [384, 2, 1, 1, 2, 1, 6, 1, 2, 2, 1, 2, 1],
        [355, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2],
        [354, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2],
        [384, 2, 1, 2, 3, 2, 1, 1, 2, 2, 1, 2, 2],
        [354, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2],
        [384, 2, 1, 2, 2, 1, 1, 2, 1, 1, 4, 2, 2],
        [354, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2],
        [354, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1],
        [385, 2, 1, 2, 2, 1, 4, 2, 2, 1, 2, 1, 2],
        [354, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1],
        [355, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2],
        [384, 1, 2, 1, 1, 4, 1, 2, 2, 1, 2, 2, 2],
        [354, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2],
        [354, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2],
        [383, 1, 2, 4, 2, 1, 2, 1, 1, 2, 1, 2, 1],
        [355, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2],
        [384, 1, 2, 2, 1, 2, 2, 1, 4, 2, 1, 1, 2],
        [355, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2],
        [354, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1],
        [384, 2, 1, 1, 2, 3, 2, 2, 1, 2, 2, 2, 1],
        [354, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1],
        [354, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1],
        [384, 2, 2, 2, 3, 2, 1, 1, 2, 1, 2, 1, 2],
        [354, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
        [355, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2],
        [384, 1, 4, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        [354, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1],
        [385, 2, 1, 2, 1, 2, 1, 4, 2, 2, 1, 2, 2],
        [354, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2],
        [354, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2],
        [384, 2, 2, 1, 1, 4, 1, 2, 1, 2, 1, 2, 2],
        [354, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2],
        [354, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1],
        [384, 2, 1, 6, 2, 1, 2, 1, 1, 2, 1, 2, 1],
        [355, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        [384, 1, 2, 1, 2, 1, 2, 1, 2, 4, 2, 1, 2],
        [354, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1],
        [355, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2],
        [384, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 2, 2],
        [354, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2],
        [354, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2],
        [384, 2, 1, 2, 4, 2, 1, 1, 2, 1, 2, 1, 2],
        [354, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [355, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2],
        [384, 1, 4, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2],
        [354, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1],
        [384, 2, 1, 2, 1, 1, 4, 2, 1, 2, 2, 2, 1],
        [355, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2],
        [354, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2],
        [383, 1, 2, 2, 1, 4, 1, 2, 1, 1, 2, 2, 1],
        [355, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2],
        [354, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1],
        [384, 2, 1, 4, 2, 1, 2, 2, 1, 2, 1, 2, 1],
        [355, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2],
        [384, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 4, 2],
        [354, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1],
        [354, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2],
        [384, 2, 2, 1, 2, 1, 5, 1, 1, 2, 2, 1, 2],
        [354, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2],
        [354, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1],
        [384, 2, 2, 1, 2, 4, 2, 1, 2, 1, 2, 1, 1],
        [355, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1],
        [355, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2],
        [384, 1, 4, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2],
        [354, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2],
        [384, 2, 1, 2, 1, 1, 2, 3, 2, 1, 2, 2, 2],
        [354, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2],
        [354, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2],
        [384, 2, 1, 2, 2, 5, 1, 2, 1, 1, 2, 1, 2],
        [354, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1],
        [355, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1]
]

MAX_YEAR_NUMBER = 150

KOREAN_CALENDAR = 0
CALENDAR_TYPE = KOREAN_CALENDAR
CALENDAR_YEAR_INFO_MAP = {
    KOREAN_CALENDAR: KOREAN_LUNAR_YEAR_INFO
}

LUNARDAYS_FOR_MONTHTYPE = {
    1: [29, 29, 0],
    2: [30, 30, 0],
    3: [58, 29, 29],
    4: [59, 30, 29],
    5: [59, 29, 30],
    6: [60, 30, 30]
}


class LunarDate(object):
    _start_date = datetime.date(1900, 1, 31)

    def __init__(self, year, month, day, is_leap_month=False):
        self.year = year
        self.month = month
        self.day = day
        self.is_leap_month = is_leap_month

    def __str__(self):
        return '%4d%02d%02d' % (self.year, self.month, self.day)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def lunardays_for_type(month_type):
        return LUNARDAYS_FOR_MONTHTYPE[month_type]

    @staticmethod
    def year_info_map():
        return CALENDAR_YEAR_INFO_MAP[CALENDAR_TYPE]

    @staticmethod
    def from_solar(year, month, day):
        if year < 1900 or year > 2050:
            raise InvalidInputRangeError("%d should be in 1900~2050" % year)

        solar_date = datetime.date(year, month, day)
        days = (solar_date - LunarDate._start_date).days

        return LunarDate.from_days(days)

    @staticmethod
    def is_in_this_days(days, left_days):
        return (days - left_days) < 0

    @staticmethod
    def is_not_in_this_days(days, left_days):
        return LunarDate.is_in_this_days(days, left_days) == False

    @staticmethod
    def from_days(days):
        start_year = 1900
        target_month = 0
        is_leap_month = False
        matched = False

        year_info = LunarDate.year_info_map()

        for year_idx in range(MAX_YEAR_NUMBER):
            year_days = year_info[year_idx][0]
            if LunarDate.is_in_this_days(days, year_days):
                for month_idx in range(12):
                    total, normal, leaf = LunarDate.lunardays_for_type(
                                              year_info[year_idx][month_idx+1])
                    if LunarDate.is_in_this_days(days, total):
                        if LunarDate.is_not_in_this_days(days, normal):
                            days -= normal
                            is_leap_month = True

                        matched = True
                        break

                    days -= total
                    target_month += 1

            if matched:
                break

            days -= year_days

        return LunarDate(start_year + year_idx, target_month + 1,
                         days + 1, is_leap_month)

    def solar(self):
        return LunarDate.to_solar(self.year, self.month,
                                  self.day, self.is_leap_month)

    @staticmethod
    def to_solar(year, month, day, is_leap_month = False):
        if year < 1900 or year > 2050:
            raise InvalidInputRangeError("%d should be in 1900~2050" % year)

        days = 0
        year_diff = year - 1900
        year_info = LunarDate.year_info_map()

        for year_idx in range(year_diff):
            days += year_info[year_idx][0]
        
        for month_idx in range(month-1):
            total, normal, leaf = LunarDate.lunardays_for_type(
                                              year_info[year_diff][month_idx+1])
            days += total

        days += (day-1)

        if is_leap_month and year_info[year_diff][month] > 2:
            days += LunarDate.lunardays_for_type(year_info[year_diff][month])[1]

        solar_date = LunarDate._start_date + datetime.timedelta(days=days)

        return solar_date
