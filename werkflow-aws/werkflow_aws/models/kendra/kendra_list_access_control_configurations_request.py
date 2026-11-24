from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraListAccessControlConfigurationsRequest(BaseModel):
    IndexId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
