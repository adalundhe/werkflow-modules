from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightTopicSearchFilter(BaseModel):
    Operator: Literal['StringEquals', 'StringLike']
    Name: Literal['QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'TOPIC_NAME']
    Value: StrictStr
