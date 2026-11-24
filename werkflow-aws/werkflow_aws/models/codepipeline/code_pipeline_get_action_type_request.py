from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineGetActionTypeRequest(BaseModel):
    category: Literal['Source', 'Build', 'Deploy', 'Test', 'Invoke', 'Approval', 'Compute']
    owner: StrictStr
    provider: StrictStr
    version: StrictStr
