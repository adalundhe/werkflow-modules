from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAgreementAvailability(BaseModel):
    status: StrictStr | None = None
    errorMessage: StrictStr | None = None
