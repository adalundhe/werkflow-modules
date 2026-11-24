from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListCampaignsRequest(BaseModel):
    solutionArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
