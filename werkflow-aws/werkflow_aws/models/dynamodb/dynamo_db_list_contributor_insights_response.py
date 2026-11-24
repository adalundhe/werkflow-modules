from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_contributor_insights_summary import DynamoDBContributorInsightsSummary


class DynamoDBListContributorInsightsResponse(BaseModel):
    ContributorInsightsSummaries: list[DynamoDBContributorInsightsSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
