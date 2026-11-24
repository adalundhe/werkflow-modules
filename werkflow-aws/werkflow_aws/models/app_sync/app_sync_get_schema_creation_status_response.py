from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AppSyncGetSchemaCreationStatusResponse(BaseModel):
    status: StrictStr | None = None
    details: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
