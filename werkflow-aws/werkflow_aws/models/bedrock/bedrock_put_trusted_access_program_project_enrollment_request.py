from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockPutTrustedAccessProgramProjectEnrollmentRequest(BaseModel):
    programIdentifier: StrictStr
    projectIdentifier: StrictStr
    optIn: Literal['inherit', 'enabled', 'disabled']
