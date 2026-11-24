from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListGlossaryTermsRequest(BaseModel):
    GlossaryIdentifier: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
