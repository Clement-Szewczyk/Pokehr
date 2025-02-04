import enum
from card_deck import Card, Deck, Color, Value


class Combinaison(enum.Enum):
    SUITE_COULEUR = 9
    CARRE = 8
    FULL = 7
    COULEUR = 6
    SUITE = 5
    BRELAN = 4
    DOUBLE_PAIRES = 3
    PAIRE = 2
    RIEN = 1


SAMPLE_RESULTS = (
    (Combinaison.SUITE_COULEUR, (Color.P, Value.VALET)),
    (Combinaison.CARRE, (Value.NEUF, Value.AS)),
    (Combinaison.FULL, (Value.SEPT, Value.ROI)),
    (Combinaison.SUITE, (Value.AS,)),
    (Combinaison.SUITE, (Value.CINQ,)),
    (Combinaison.COULEUR, (Color.K, Value.DAME,
                           Value.VALET, Value.HUIT, Value.SIX, Value.CINQ)),
    (Combinaison.BRELAN, (Value.VALET, Value.QUATRE, Value.DEUX)),
    (Combinaison.DOUBLE_PAIRES, (Value.ROI, Value.TROIS, Value.CINQ)),
    (Combinaison.PAIRE, (Value.ROI, Value.AS, Value.DIX, Value.SEPT)),
    (Combinaison.RIEN, (Value.AS, Value.DAME, Value.DIX, Value.HUIT, Value.SIX)),
)
