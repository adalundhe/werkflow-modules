from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightDataSourceSearchFilter(BaseModel):
    Operator: Literal['StringEquals', 'StringLike']
    Name: Literal['DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DATASOURCE_NAME']
    Value: StrictStr
