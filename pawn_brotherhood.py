"""

  Created on 12/15/2016 by Ben

  benuklove@gmail.com
  
  Solution to Pawn Brotherhood on CheckiO.
  Determines number of safe pawns given a set of pawns with chess coordinates.

"""

pawns = ({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
# pawns = ({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
# pawns = ({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"})
# pawns = ({"b4"})

pawndict = dict.fromkeys(pawns, 0)
print(pawndict)

for item in pawndict:
    for other_item in pawns:
        if int(other_item[1]) == (int(item[1]) - 1) and \
            (int(ord(other_item[0])) == int(ord(item[0]) - 1) or
                int(ord(other_item[0])) == int((ord(item[0]) + 1))):
            pawndict[item] = 1

safepawns = sum(pawndict.values())
print(pawndict)

if len(pawns) == 0:
    safepawns = 0
elif len(pawns) == 1:
    safepawns = 0

print(safepawns)
