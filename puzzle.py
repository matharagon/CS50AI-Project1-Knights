from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
   # These are the conditions that say that A can be and only be either a Knight or a Knave.
   Not(And(AKnight, AKnave)), Or(AKnave, AKnight), 

   # This is the sentence above in logical sentence. Since all of these sentences have to be True, it suffices to check when A is Knight.
   Implication(AKnight, And(AKnight,AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
   # These are the conditions that say that A and B can be and only be either a Knight or a Knave.
   Not(And(AKnight, AKnave)),  Or(AKnave, AKnight), 
   Not(And(BKnight, BKnave)), Or(BKnave, BKnight), 

   # Since B says nothing, we tell the AI to check the cases for which A is a Knight and a Knave, the second case denies the conclusion of the first. 
   Implication(AKnight, And(AKnave, BKnave)), 
   Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # These are the conditions that say that A and B can be and only be either a Knight or a Knave.
    Not(And(AKnight, AKnave)),  Or(AKnave, AKnight), 
    Not(And(BKnight, BKnave)), Or(BKnave, BKnight), 

    # Translating the sentences considering all possible cases for A and B in order to let the AI decide.
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # These are the conditions that say that A and B be and can only be either a Knight or a Knave.
    Not(And(AKnight, AKnave)),  Or(AKnave, AKnight),
    Not(And(BKnight, BKnave)), Or(BKnave, BKnight),

    # The case for which A is a Knight is represented by the line 57. C is determined by A and B, hence the AI concludes that what C is.
    # All other sentences have been translated to logical sentences respectively.

    Implication(AKnave, Not(And(Not(And(AKnight, AKnave)), Or(AKnave, AKnight)))),
    Implication(BKnight, AKnave),  
    Implication(BKnight, CKnave), 
    Implication(BKnave, CKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
