from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMComplianceStringFilter(BaseModel):
    Key: StrictStr | None = None
    Values: list[StrictStr] | None = None
    Type: Literal['EQUAL', 'NOT_EQUAL', 'BEGIN_WITH', 'LESS_THAN', 'GREATER_THAN'] | None = None
