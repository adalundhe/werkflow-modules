from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBContributorInsightsSummary(BaseModel):
    TableName: StrictStr | None = None
    IndexName: StrictStr | None = None
    ContributorInsightsStatus: StrictStr | None = None
    ContributorInsightsMode: StrictStr | None = None
