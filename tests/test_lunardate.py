from lunardate import LunarDate


class TestLunarDate(object):
    def test_lunar_19790922_from_solar_19791111(self):
        date = LunarDate.from_solar(1979, 11, 11)
        assert date.year == 1979
        assert date.month == 9
        assert date.day == 22
        assert date.is_leap_month is False

    def test_lunar_19000101_from_solar_19000131(self):
        date = LunarDate.from_solar(1900, 1, 31)
        assert date.year == 1900
        assert date.month == 1
        assert date.day == 1
        assert date.is_leap_month is False

    def test_lunar_19020101_from_solar_19020208(self):
        date = LunarDate.from_solar(1902, 2, 8)
        assert date.year == 1902
        assert date.month == 1
        assert date.day == 1
        assert date.is_leap_month is False

    def test_lunar_19040101_from_solar_19040216(self):
        date = LunarDate.from_solar(1904, 2, 16)
        assert date.year == 1904
        assert date.month == 1
        assert date.day == 1
        assert date.is_leap_month is False

    def test_lunar_20140930_from_solar_20141023(self):
        date = LunarDate.from_solar(2014, 10, 23)
        assert date.year == 2014
        assert date.month == 9
        assert date.day == 30
        assert date.is_leap_month is False

    def test_lunar_19870621_from_solar_19870815_leap(self):
        date = LunarDate.from_solar(1987, 8, 15)
        assert date.year == 1987
        assert date.month == 6
        assert date.day == 21
        assert date.is_leap_month is True

    # 3rd MONTHTYPE test case
    def test_lunar_20171025_from_solar_20171212(self):
        date = LunarDate.from_solar(2017, 12, 12)
        assert date.year == 2017
        assert date.month == 10
        assert date.day == 25
        assert date.is_leap_month is False

    # 4th MONTHTYPE test case
    def test_lunar_19870729_from_solar_19870921(self):
        date = LunarDate.from_solar(1987, 9, 21)
        assert date.year == 1987
        assert date.month == 7
        assert date.day == 29
        assert date.is_leap_month is False

    # 5th MONTHTYPE test case
    def test_lunar_19551119_from_solar_19560101(self):
        date = LunarDate.from_solar(1956, 1, 1)
        assert date.year == 1955
        assert date.month == 11
        assert date.day == 19
        assert date.is_leap_month is False
