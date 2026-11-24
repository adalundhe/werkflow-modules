from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessGetIngestionStreamRequest(BaseModel):
    collectionId: StrictStr
    ingestionStreamId: StrictStr
