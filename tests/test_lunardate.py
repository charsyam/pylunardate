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
