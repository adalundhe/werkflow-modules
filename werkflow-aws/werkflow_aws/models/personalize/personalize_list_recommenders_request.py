from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListRecommendersRequest(BaseModel):
    datasetGroupArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
