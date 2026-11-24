from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailListImportFailuresRequest(BaseModel):
    ImportId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
