from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DynamoDBUpdateContributorInsightsRequest(BaseModel):
    TableName: StrictStr
    ContributorInsightsAction: Literal['ENABLE', 'DISABLE']
    IndexName: StrictStr | None = None
    ContributorInsightsMode: Literal['ACCESSED_AND_THROTTLED_KEYS', 'THROTTLED_KEYS'] | None = None
