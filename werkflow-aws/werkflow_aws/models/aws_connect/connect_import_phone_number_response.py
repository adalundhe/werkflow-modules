from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectImportPhoneNumberResponse(BaseModel):
    PhoneNumberId: StrictStr | None = None
    PhoneNumberArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
