"""
Wordcount support library

A support library for the ranger wordcount linemode plugin
"""
import os
import re
import subprocess

from logging import getLogger

LOG = getLogger(__name__)


def dummy_bytesize_func(
    value: float | str,
    binary: bool = False,
    gnu: bool = False,
    format: str = "%.1f",
) -> str:
    """
    Dummy bytesize_func to substitute in if none of the bytesize
    conversion modules are found.
    """
    return ""


try:
    LOG.debug("trying to import humanize")
    import humanize

    bytesize_func = humanize.naturalsize
except ImportError:
    LOG.debug("trying to import bytesize")
    try:
        import bytesize

        bytesize_func = bytesize.bytesize.Size
    except ImportError:
        bytesize_func = dummy_bytesize_func


class WCHelper:
    """
    Helper class that provides support routines to ranger_wc
    """

    # Set the default max file size to check to 100kB
    max_wc_file_size = 1000 * 100
    # Show in the linemode if the files are too large to parse
    show_large_size = True

    def __init__(self):
        "Initialize a WCHelper class that provides services to the WCLinemode plugin"
        # Compile a regular expression matcher to parse the wc output
        # Capture the second field, which is the number of words in the file
        # This may be platform-dependent
        self.matcher = re.compile(r"\s+[0-9]+\s+([0-9]+)\s+[0-9]+.*")
        self.bytesize_func = bytesize_func

    def size_as_bytesize(self, size: float | str) -> str:
        "Return the size as a bytesize string"
        bs = bytesize_func(size)
        return str(bs)

    # TODO: Figure out how to re-use the info from ranger
    def file_size(self, filename):
        """
        Get the file size of a file
        Return None if the file is not found
        This seems to happen occasionally in ranger when changing directories.
        """
        try:
            return os.stat(filename).st_size
        except FileNotFoundError as e:
            LOG.error("ranger-wc wc_helper file_size error: {}".format(e))
            return None

    def call_wc(self, filename):
        "Call wc and return the results"
        return subprocess.run(["wc", filename], capture_output=True)

    def get_wc_string(self, res):
        "Get the string from the subprocess result"
        return str(res.stdout, encoding="utf-8")

    def get_wc(self, res):
        "Parse the word count from a wc string"
        regex_match = self.matcher.match(res)
        if regex_match:
            wc = regex_match[1]
            return wc
        else:
            return None

    def infostring(self, fobj, metadata):
        """
        Add the number of words in the file to the linemode
        Or return the empty string
        """
        size = self.file_size(fobj.relative_path)
        # Limit checking to files below a certain size
        # If we couldn't find the size, don't return an infostring
        if size is None:
            return ""
        # If the size is above our limit, indicate that
        if size > WCHelper.max_wc_file_size:
            if WCHelper.show_large_size:
                return "{}".format(self.size_as_bytesize(size))
            else:
                return ""

        # Get the number of words
        try:
            res = self.call_wc(fobj.relative_path)
        except FileNotFoundError as e:
            LOG.warning("ranger-wc wc_helper: {}".format(e))
            # Return empty string if wc is not installed
            return ""
        if res.returncode == 0:
            wc_string = self.get_wc_string(res)
            wc = self.get_wc(wc_string)
            if wc:
                return "{}".format(wc)

        return ""
