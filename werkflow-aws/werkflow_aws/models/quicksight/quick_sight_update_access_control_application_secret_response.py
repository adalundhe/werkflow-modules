from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateAccessControlApplicationSecretResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ClientSecretId: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    RegionalSecretManagerArns: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
