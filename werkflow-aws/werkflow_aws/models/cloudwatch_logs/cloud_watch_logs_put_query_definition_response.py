from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutQueryDefinitionResponse(BaseModel):
    queryDefinitionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
