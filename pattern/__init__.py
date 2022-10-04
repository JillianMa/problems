import check50
import check50.c

@check50.check()
def exists():
    """pattern.c exists"""
    check50.exists("pattern.c")

@check50.check(exists)
def compiles():
    """pattern.c compiles"""
    check50.c.compile("pattern.c", lcs50=True)
