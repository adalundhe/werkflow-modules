from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMEmailValidationChallenge(BaseModel):
    ValidationEmails: list[StrictStr] | None = None
    ValidationDomain: StrictStr | None = None
