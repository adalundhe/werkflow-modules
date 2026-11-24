from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessGetIngestionJobRequest(BaseModel):
    collectionId: StrictStr
    ingestionJobId: StrictStr
