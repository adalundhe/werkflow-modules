from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectTagSearchCondition(BaseModel):
    tagKey: StrictStr | None = None
    tagValue: StrictStr | None = None
    tagKeyComparisonType: Literal['STARTS_WITH', 'CONTAINS', 'EXACT'] | None = None
    tagValueComparisonType: Literal['STARTS_WITH', 'CONTAINS', 'EXACT'] | None = None
