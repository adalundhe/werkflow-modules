from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListGlossariesRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
