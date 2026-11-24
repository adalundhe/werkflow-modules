from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockStartTrustedAccessProgramProjectApplicationRequest(BaseModel):
    programIdentifier: StrictStr
    projectIdentifier: StrictStr
