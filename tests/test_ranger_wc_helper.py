import os
import subprocess
from unittest import mock

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

def test_wc_helper_file_size(mocker):
    # Test getting the file size
    sr = os.stat_result((0, 0, 0, 0, 0, 0, 1000 * 101, 0, 0, 0))
    mocker.patch("os.stat", return_value=sr)
    wc_helper = WCHelper()
    fs = wc_helper.file_size("blah.txt")
    assert fs == 1000 * 101

class FObj:
    def __init__(self, relative_path):
        self.relative_path = relative_path

def test_wc_infostring_invalid_file(mocker):
    # Test getting the file size
    mocker.patch("os.stat", side_effect=FileNotFoundError("file not found"))
    wc_helper = WCHelper()
    fs = wc_helper.file_size("blah.txt")
    assert fs is None

    fobj = FObj("blah.txt")
    res = wc_helper.infostring(fobj, None)
    assert res == ""

def test_wc_infostring_small_file(mocker):
    # Test valid file within limits
    wc_helper = WCHelper()
    fobj = FObj("test-data.txt")
    res = wc_helper.infostring(fobj, None)
    assert res == "3"

def test_wc_no_wc_installed(mocker):
    # Test on a system without wc
    mocker.patch("subprocess.run",
                 side_effect=FileNotFoundError("No such file or directory: 'wc'"))
    wc_helper = WCHelper()
    fobj = FObj("test-data.txt")
    res = wc_helper.infostring(fobj, None)
    assert res == ""

def test_wc_infotitle_invalid_file_after_stat(mocker):
    # Test the case where stat finds the file, but wc doesn't
    # This catches situations where the file is deleted or moved after the
    # size test but before wc is run
    wc_helper = WCHelper()
    fobj = FObj("test-data.txt")
    mocker.patch("subprocess.run",
                 return_value=subprocess.CompletedProcess(
                     args=['wc', 'test-data.txt'],
                     returncode=1, stdout=b'',
                     stderr=b'wc: test-data.txt: No such file or directory\n'))
    res = wc_helper.infostring(fobj, None)
    assert res == ""

def test_wc_infostring_large_file(mocker):
    # Test valid file within limits
    sr = os.stat_result((0, 0, 0, 0, 0, 0, WCHelper.max_wc_file_size + 1, 0, 0, 0))
    mocker.patch("os.stat", return_value=sr)
    wc_helper = WCHelper()
    fobj = FObj("test-data.txt")
    res = wc_helper.infostring(fobj, None)

    try:
        import humanize
        assert res == "100.0 kB"
    except ModuleNotFoundError:
        import bytesize
        assert res == "97.66 KiB"
    except ModuleNotFoundError:
        assert False
