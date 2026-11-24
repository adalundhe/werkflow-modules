from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockStartTrustedAccessProgramOrganizationApplicationRequest(BaseModel):
    programIdentifier: StrictStr
