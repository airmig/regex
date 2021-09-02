import concurrent.futures
import logging
import re
"""
pytest tool to test regular expression

[] match a assert
A|C == [AC]
. any character (does not include special chars)
\W \w special chars
\d digit
\D non digit
\s whitespace \S non whitespace
t = r
^ begin \A only beginning
$ end
\b boundary \B

* 0 or more
+ one or more
? zero or one
{m,n} between m and n, inclusive

(?) conditional
(? cond | cond)
(?=t)  look ahead ex: writing took    (does not include t)
(?!) negative look ahead
(?<) look behind have to be fixed length
(?<!) negative look behind
(?#) comment
not greedy use ?

use () for grouping

.match beginning of string
.fullmatch string fully matches

?P<named group>
\1 refers to the first group
"""
class BasicLogger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
        logging.info("Basic logger has been configured")


def init():
    logger = BasicLogger()
    logging.info("Regex project initialized")
    return True


def thread():
    logging.info("Main thread initialized")
    question = "Lovely spam! Wonderful spam!"
    rc = re.search("spam", question)
    logging.info(f"Search string: {rc.string}")
    logging.info(f"Search result: {bool(rc)}")
    logging.info(f"Boundary: {rc.span()}")
    logging.info(f"Lower: {rc.start()}")
    logging.info(f"Upper: {rc.end()}")
    logging.info(rc)

    #finds all returns alist
    rc = re.findall("[aeiou][^aeiou]", question)
    #.finditer returns an iterator more effecient for large number of matches
    logging.info(rc)

    #.group returns the matched group or a tuple of matched groups
    #.groups all the matched groups
    #group 0 is the whole match
    rc = re.search(r"(?P<first>\w+),(?P<second>\w+)","one,two,three")
    logging.info(rc)
    logging.info(rc.groups())
    logging.info(rc.group(2))
    logging.info(rc.group(1,2))
    logging.info(rc.groupdict())
    result = rc.expand("second was '\g<2>', first was '\g<1>'")
    logging.info(result)

    content = "My favorite numbers are 13 and 14"
    #use count to repla
    rc = re.sub(r"\d+", '#', content)
    logging.info(content)
    logging.info(rc)

    def reverse(match):
        logging.info(match)
        logging.info(match.group(0))
        return match.group(0)[::-1]

    result = re.sub(r"\d+", reverse, content)
    logging.info(result)
    result = re.sub(r"(\d+)", r"\g<1>0", "is this a 1?")
    logging.info(result)

    #using subn returns total of subs
    result = re.sub(r"x*", "-", "spam")
    logging.info(result)
    result = re.subn(r"x*", "-", "spam")
    logging.info(result)

    # use maxsplit parameter to specify number of splits
    result = re.split(r"\d+", "my favs are 1 and 2")
    logging.info(result)

    result = re.split(r"(\d+)", "my favs are 1 and 2")
    logging.info(result)

    #use re.escape to clean up a string
    #use re.compile to resuse regex
    logging.info("Finished main thread")

    # flags
    # re.I  re.IGNORECASE case insensitive
    # re.M  re.MULTILINE use multiline
    # re.S  re.DOTALL . matches new line
    # re.X  re.VERBOSE allows whitespace and comments in Regex

    # re.ASCII, re.UNICODE(default python 3), re.LOCALE


if __name__ == "__main__":
    init()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        e.submit(thread)
    logging.info("Program has ended")
