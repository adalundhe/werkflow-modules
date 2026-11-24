from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightSearchFlowsFilter(BaseModel):
    Name: Literal['assetName', 'assetDescription', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER']
    Operator: Literal['StringEquals', 'StringLike']
    Value: StrictStr
