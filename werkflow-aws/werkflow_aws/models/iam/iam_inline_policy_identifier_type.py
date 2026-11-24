from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IAMInlinePolicyIdentifierType(BaseModel):
    PolicyName: StrictStr
    AttachmentType: Literal['user', 'group', 'role']
    AttachmentName: StrictStr
