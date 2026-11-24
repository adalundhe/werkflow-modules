from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetTrustedAccessProgramOrganizationEnrollmentRequest(BaseModel):
    programIdentifier: StrictStr
