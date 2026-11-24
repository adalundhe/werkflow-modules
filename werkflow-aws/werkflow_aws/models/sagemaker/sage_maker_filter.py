from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerFilter(BaseModel):
    Name: StrictStr
    Operator: Literal['Equals', 'NotEquals', 'GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo', 'Contains', 'Exists', 'NotExists', 'In'] | None = None
    Value: StrictStr | None = None
