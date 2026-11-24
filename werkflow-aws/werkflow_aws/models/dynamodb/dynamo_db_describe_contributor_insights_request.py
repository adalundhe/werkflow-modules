from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeContributorInsightsRequest(BaseModel):
    TableName: StrictStr
    IndexName: StrictStr | None = None
