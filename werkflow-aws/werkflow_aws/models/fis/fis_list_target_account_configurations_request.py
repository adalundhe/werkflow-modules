from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FISListTargetAccountConfigurationsRequest(BaseModel):
    experimentTemplateId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
