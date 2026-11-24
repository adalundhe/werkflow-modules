from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightAgentSearchFilter(BaseModel):
    Name: Literal['DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'AGENT_NAME'] | None = None
    Operator: Literal['StringEquals', 'StringLike'] | None = None
    Value: StrictStr | None = None
