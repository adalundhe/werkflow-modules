from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCancelIngestionJobResponse(BaseModel):
    ingestionJobId: StrictStr | None = None
    collectionId: StrictStr | None = None
    ingestionJobName: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
