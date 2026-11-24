from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListIterableFormsRequest(BaseModel):
    AssetIdentifier: StrictStr
    IterableFormName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
