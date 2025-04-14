from typing import Literal


MatchOptionTypes = Literal[
    "EQUALS",
    "ABSENT",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "CASE_SENSITIVE",
    "CASE_INSENSITIVE",
    "GREATER_THAN_OR_EQUAL",
]
