from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListAliasesRequest(BaseModel):
    ImageName: StrictStr
    Alias: StrictStr | None = None
    Version: StrictInt | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
