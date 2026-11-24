from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class DataPipelineQueryObjectsResponse(BaseModel):
    ids: list[StrictStr] | None = None
    marker: StrictStr | None = None
    hasMoreResults: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
