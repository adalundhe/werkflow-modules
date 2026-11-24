from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineApprovalResult(BaseModel):
    summary: StrictStr
    status: Literal['Approved', 'Rejected']
