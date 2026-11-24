from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetTrustedAccessProgramAccountEnrollmentRequest(BaseModel):
    programIdentifier: StrictStr
