import ranger.api
from ranger.core.linemode import LinemodeBase

from .wc_helper import WCHelper

@ranger.api.register_linemode
class WCLinemode(LinemodeBase):
    name = "wc"
    uses_metadata = False

    def __init__(self):
        self.wc_helper = WCHelper()

    def call_wc(self, filename):
        "Call wc and return the results"
        return self.wc_helper.call_wc(filename)

    def get_wc_string(self, res):
        "Convert the wc result to a string"
        return self.wc_helper.get_wc_string(res)

    def get_wc(self, res):
        "Parse the word count from the wc process call"
        return self.wc_helper.get_wc(res)

    def filetitle(self, fobj, metadata):
        return fobj.relative_path
    
    def infostring(self, fobj, metadata):
        """
        Add the number of words in the file to the linemode
        Or return the empty string
        """
        return self.wc_helper.infostring(fobj, metadata)
