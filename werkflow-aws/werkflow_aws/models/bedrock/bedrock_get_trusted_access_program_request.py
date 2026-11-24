from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetTrustedAccessProgramRequest(BaseModel):
    programIdentifier: StrictStr
    projectIdentifier: StrictStr | None = None
