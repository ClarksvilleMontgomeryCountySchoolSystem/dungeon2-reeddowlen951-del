good = r""" __      _.._
       .-'__`-._.'.--.'.__.,
      /--'  '-._.'    '-._./
     /__.--._.--._.'``-.__/
     '._.-'-._.-._.-''-..'"""
bad = r"""______________________________
\                             \           _         ______ |
 \                             \        /   \___-=O`/|O`/_>|
  \                             \_______\ RFA      / | /    )
  /                             /        `/-==__ _/__|/__=-|
 /                             /         *             \ | |
/_____________________________/                        (o)"""
escaped = True
if escaped:
    outcome = ("Legend: We made it!")
    print(good)
else:
    outcome = ("Doom: We got caught!")
    print(bad)
print(outcome)