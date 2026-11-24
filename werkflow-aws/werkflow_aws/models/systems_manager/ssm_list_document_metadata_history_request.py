from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SSMListDocumentMetadataHistoryRequest(BaseModel):
    Name: StrictStr
    Metadata: Literal['DocumentReviews']
    DocumentVersion: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
