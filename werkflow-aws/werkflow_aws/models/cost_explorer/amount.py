import re
from pydantic import StrictFloat, BeforeValidator
from typing import Annotated

numeric_pattern = re.compile(r'(\d+.\d+)|(\d+)')

def prepare_amount(value: str | float) -> float:
    value = value.lstrip('-')
    if isinstance(value, str) and (
        amount := re.match(
            numeric_pattern,
            value,
        )
    ):
        return float(amount.group(0))

    return value


Amount = Annotated[
    StrictFloat,
    BeforeValidator(prepare_amount),
]