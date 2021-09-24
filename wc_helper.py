# Wordcount support library
import re, subprocess

class WCHelper:
    """
    Abstract out most of the code to a helper class
    """
    def __init__(self):
        # Compile a regular expression matcher to parse the wc output
        # Capture the second field, which is the number of words in the file
        # This may be platform-dependent
        self.matcher = re.compile(r"\s+[0-9]+\s+([0-9]+)\s+[0-9]+.*")

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


