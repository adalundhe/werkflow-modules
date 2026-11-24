from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightSpaceQuicksightSearchFilter(BaseModel):
    name: Literal['SPACE_ID', 'SPACE_NAME', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'CONTRIBUTED_BY', 'CONSUMED_SOURCE_SIZE', 'CREATED_BY']
    operator: Literal['STRING_EQUALS', 'STRING_LIKE', 'NUMBER_RANGE']
    value: StrictStr
