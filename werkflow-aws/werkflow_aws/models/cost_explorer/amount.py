from typing import Annotated
from pydantic import BeforeValidator, StrictFloat


def prepare_amount(value: str | int | float) -> float:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    if isinstance(value, str):
        return float(value.strip())
    return value


Amount = Annotated[
    StrictFloat,
    BeforeValidator(prepare_amount),
]
