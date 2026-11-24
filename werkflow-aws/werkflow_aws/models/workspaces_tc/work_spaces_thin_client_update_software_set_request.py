from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientUpdateSoftwareSetRequest(BaseModel):
    id: StrictStr
    validationStatus: Literal['VALIDATED', 'NOT_VALIDATED']
