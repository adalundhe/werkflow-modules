from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueUpdateAssetResponse(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
