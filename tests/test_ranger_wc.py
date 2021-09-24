import pytest
from wc_helper import WCHelper

def test_call_wc_invalid_file():
    # Test trying to read an invalid file
    wc_helper = WCHelper()

    res = wc_helper.call_wc("blah.txt")
    assert res.returncode == 1
    assert len(res.stdout) == 0
    assert len(res.stderr) > 0

def test_call_wc_valid_file():
    # Test trying to to read a valid file
    wc_helper = WCHelper()

    res = wc_helper.call_wc("test-data.txt")
    assert res.returncode == 0
    assert len(res.stdout) > 0
    assert len(res.stderr) == 0
    assert str(res.stdout, encoding="utf-8") == " 1  3 16 test-data.txt\n"

def test_get_wc_string():
    # Test trying to convert subprocess result to a string
    wc_helper = WCHelper()

    res = wc_helper.call_wc("test-data.txt")
    assert wc_helper.get_wc_string(res) == " 1  3 16 test-data.txt\n"

def test_get_wc():
    # Test parsing the result
    wc_helper = WCHelper()
    res = wc_helper.call_wc("test-data.txt")
    s = wc_helper.get_wc_string(res)
    res = wc_helper.get_wc(s)
    assert res == "3"
