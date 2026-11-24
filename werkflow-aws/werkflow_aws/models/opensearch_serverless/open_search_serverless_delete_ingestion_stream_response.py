from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessDeleteIngestionStreamResponse(BaseModel):
    ingestionStreamId: StrictStr | None = None
    collectionId: StrictStr | None = None
    ingestionStreamName: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
