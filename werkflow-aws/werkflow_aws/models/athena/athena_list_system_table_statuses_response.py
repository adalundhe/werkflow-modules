from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_system_table_status import AthenaSystemTableStatus


class AthenaListSystemTableStatusesResponse(BaseModel):
    Items: list[AthenaSystemTableStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
