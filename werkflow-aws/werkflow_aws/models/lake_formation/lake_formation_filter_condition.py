from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LakeFormationFilterCondition(BaseModel):
    Field: Literal['RESOURCE_ARN', 'ROLE_ARN', 'LAST_MODIFIED'] | None = None
    ComparisonOperator: Literal['EQ', 'NE', 'LE', 'LT', 'GE', 'GT', 'CONTAINS', 'NOT_CONTAINS', 'BEGINS_WITH', 'IN', 'BETWEEN'] | None = None
    StringValueList: list[StrictStr] | None = None
