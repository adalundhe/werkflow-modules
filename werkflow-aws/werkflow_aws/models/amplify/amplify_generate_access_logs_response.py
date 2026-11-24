from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AmplifyGenerateAccessLogsResponse(BaseModel):
    logUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
