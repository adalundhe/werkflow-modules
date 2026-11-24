from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightActionConnectorSearchFilter(BaseModel):
    Name: Literal['ACTION_CONNECTOR_NAME', 'ACTION_CONNECTOR_TYPE', 'QUICKSIGHT_OWNER', 'QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER']
    Operator: Literal['StringEquals', 'StringLike']
    Value: StrictStr
