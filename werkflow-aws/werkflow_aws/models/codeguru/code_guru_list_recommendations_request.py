from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeGuruListRecommendationsRequest(BaseModel):
    CodeReviewArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
