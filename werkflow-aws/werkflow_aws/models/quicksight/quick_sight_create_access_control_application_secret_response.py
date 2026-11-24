from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateAccessControlApplicationSecretResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ClientSecretId: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
