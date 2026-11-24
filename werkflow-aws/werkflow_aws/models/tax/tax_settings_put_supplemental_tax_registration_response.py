from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class TaxSettingsPutSupplementalTaxRegistrationResponse(BaseModel):
    authorityId: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
