from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineDeleteCustomActionTypeRequest(BaseModel):
    category: Literal['Source', 'Build', 'Deploy', 'Test', 'Invoke', 'Approval', 'Compute']
    provider: StrictStr
    version: StrictStr
