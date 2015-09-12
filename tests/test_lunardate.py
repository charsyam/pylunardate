from lunardate import LunarDate


class TestLunarDate(object):
    def test_lunar_19790922_from_solar_19791111_two_way(self):
        date = LunarDate.from_solar(1979, 11, 11)
        assert date.year == 1979
        assert date.month == 9
        assert date.day == 22
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(1979, 9, 22, False)
        assert solar_date.year == 1979
        assert solar_date.month == 11
        assert solar_date.day == 11

    def test_lunar_19000101_from_solar_19000131_two_way(self):
        date = LunarDate.from_solar(1900, 1, 31)
        assert date.year == 1900
        assert date.month == 1
        assert date.day == 1
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(1900, 1, 1, False)
        assert solar_date.year == 1900
        assert solar_date.month == 1
        assert solar_date.day == 31

    def test_lunar_19020101_from_solar_19020208_two_way(self):
        date = LunarDate.from_solar(1902, 2, 8)
        assert date.year == 1902
        assert date.month == 1
        assert date.day == 1
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(1902, 1, 1, False)
        assert solar_date.year == 1902
        assert solar_date.month == 2
        assert solar_date.day == 8

    def test_lunar_19040101_from_solar_19040216_two_way(self):
        date = LunarDate.from_solar(1904, 2, 16)
        assert date.year == 1904
        assert date.month == 1
        assert date.day == 1
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(1904, 1, 1, False)
        assert solar_date.year == 1904
        assert solar_date.month == 2
        assert solar_date.day == 16

    def test_lunar_20140930_from_solar_20141023_two_way(self):
        date = LunarDate.from_solar(2014, 10, 23)
        assert date.year == 2014
        assert date.month == 9
        assert date.day == 30
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(2014, 9, 30, False)
        assert solar_date.year == 2014
        assert solar_date.month == 10
        assert solar_date.day == 23

    def test_lunar_19870621_from_solar_19870815_leap_two_way(self):
        date = LunarDate.from_solar(1987, 8, 15)
        assert date.year == 1987
        assert date.month == 6
        assert date.day == 21
        assert date.is_leap_month is True
        solar_date = LunarDate.to_solar(1987, 6, 21, True)
        assert solar_date.year == 1987
        assert solar_date.month == 8
        assert solar_date.day == 15


    # 3rd MONTHTYPE test case
    def test_lunar_20171025_from_solar_20171212_two_way(self):
        date = LunarDate.from_solar(2017, 12, 12)
        assert date.year == 2017
        assert date.month == 10
        assert date.day == 25
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(2017, 10, 25, False)
        assert solar_date.year == 2017
        assert solar_date.month == 12
        assert solar_date.day == 12

    # 4th MONTHTYPE test case
    def test_lunar_19870729_from_solar_19870921_two_way(self):
        date = LunarDate.from_solar(1987, 9, 21)
        assert date.year == 1987
        assert date.month == 7
        assert date.day == 29
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(1987, 7, 29, False)
        assert solar_date.year == 1987
        assert solar_date.month == 9
        assert solar_date.day == 21

    # 5th MONTHTYPE test case
    def test_lunar_19551119_from_solar_19560101_two_way(self):
        date = LunarDate.from_solar(1956, 1, 1)
        assert date.year == 1955
        assert date.month == 11
        assert date.day == 19
        assert date.is_leap_month is False
        solar_date = LunarDate.to_solar(1955, 11, 19, False)
        assert solar_date.year == 1956
        assert solar_date.month == 1
        assert solar_date.day == 1

    def test_lunar_to_solar_19550329_leap_case_check(self):
        solar_date = LunarDate.to_solar(1955, 3, 29, False)
        assert solar_date.year == 1955
        assert solar_date.month == 4
        assert solar_date.day == 21
        solar_date_leap = LunarDate.to_solar(1955, 3, 29, True)
        assert solar_date_leap.year == 1955
        assert solar_date_leap.month == 5
        assert solar_date_leap.day == 20

    def test_lunar_to_solar_20150908_not_leap_month_case_check(self):
        solar_date = LunarDate.to_solar(2015, 7, 26, False)
        assert solar_date.year == 2015
        assert solar_date.month == 9
        assert solar_date.day == 8

        solar_date_leap = LunarDate.to_solar(2015, 7, 26, True)
        assert solar_date_leap.year == 2015
        assert solar_date_leap.month == 9
        assert solar_date_leap.day == 8