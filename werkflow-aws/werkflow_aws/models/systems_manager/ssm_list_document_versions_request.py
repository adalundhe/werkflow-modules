from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMListDocumentVersionsRequest(BaseModel):
    Name: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
