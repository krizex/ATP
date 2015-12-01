from atp.log import logger_manager
import logging

# http://stackoverflow.com/questions/13131400/logging-variable-data-with-new-format-string
class BraceString(str):
    def __mod__(self, other):
        return self.format(*other)
    
class CustomAdapter(logging.LoggerAdapter):
    def __init__(self, logger, extra=None):
        super(CustomAdapter, self).__init__(logger, extra)

    def process(self, msg, kwargs):
        msg = BraceString(msg)
        return msg, kwargs
    
L = CustomAdapter(logger_manager.getLogger("atp"))

if __name__ == "__main__":
    L.debug("{} {}", "1", 2)