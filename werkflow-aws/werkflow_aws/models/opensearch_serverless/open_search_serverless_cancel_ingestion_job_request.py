from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCancelIngestionJobRequest(BaseModel):
    collectionId: StrictStr
    ingestionJobId: StrictStr
    clientToken: StrictStr | None = None
