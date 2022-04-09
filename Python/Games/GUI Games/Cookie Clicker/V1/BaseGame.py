cookies = 0
clicks = 0
# Cookies Per Click
cpc = 1
# Click Upgrade Price
cup = 100
# Cookies Per Second
cps = 0


def newClick():
    global cookies, clicks
    cookies += cpc
    clicks += 1


def canUpgrade():
    global cup
    if cup <= cookies:
        cup += 50
        return True
    else:
        return False


def upgradeCLick():
    global cpc, cookies
    cpc += 1
    cookies -= cup


def getCookies():
    return cookies


def getClicks():
    return clicks


def getCPC():
    return cpc


def getCPS():
    return cps


def getCUP():
    return cup
