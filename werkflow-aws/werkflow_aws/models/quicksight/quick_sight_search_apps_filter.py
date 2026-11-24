from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightSearchAppsFilter(BaseModel):
    Name: Literal['APP_ID', 'APP_NAME', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER']
    Operator: Literal['StringEquals', 'StringLike']
    Value: StrictStr
