from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockPutTrustedAccessProgramAccountEnrollmentRequest(BaseModel):
    programIdentifier: StrictStr
    optIn: Literal['inherit', 'enabled', 'disabled']
