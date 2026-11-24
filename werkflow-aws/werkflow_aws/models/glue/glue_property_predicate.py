from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GluePropertyPredicate(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    Comparator: Literal['EQUALS', 'GREATER_THAN', 'LESS_THAN', 'GREATER_THAN_EQUALS', 'LESS_THAN_EQUALS'] | None = None
