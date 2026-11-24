from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class RDSDownloadDBLogFilePortionResponse(BaseModel):
    LogFileData: StrictStr | None = None
    Marker: StrictStr | None = None
    AdditionalDataPending: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
