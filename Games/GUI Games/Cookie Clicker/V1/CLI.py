import BaseGame as game

Done = False

while not Done:
    game.newClick()
    if game.canUpgrade():
        game.upgradeCLick()
    if game.getCookies() >= 10000:
        Done = True

print(game.getClicks())
print(game.getCookies())
print(game.getCPC())
print(game.getCUP())
