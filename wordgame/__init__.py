import check50
import check50.c

@check50.check()
def exists():
    """wordgame.c exists"""
    check50.exists("wordgame.c")

@check50.check(exists)
def compiles():
    """wordgame.c compiles"""
    check50.c.compile("wordgame.c", lcs50=True)
