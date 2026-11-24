from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateExtractionDefinitionResponse(BaseModel):
    ExtractionDefinitionArn: StrictStr | None = None
    ExtractionDefinitionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
