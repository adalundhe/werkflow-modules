from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LightsailDownloadDefaultKeyPairResponse(BaseModel):
    publicKeyBase64: StrictStr | None = None
    privateKeyBase64: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
