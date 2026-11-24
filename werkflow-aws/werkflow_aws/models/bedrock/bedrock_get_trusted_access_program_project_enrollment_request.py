from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetTrustedAccessProgramProjectEnrollmentRequest(BaseModel):
    programIdentifier: StrictStr
    projectIdentifier: StrictStr
