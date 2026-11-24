from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3FilterRuleInput(BaseModel):
    Name: Literal['prefix', 'suffix'] | None = None
    Value: StrictStr | None = None
