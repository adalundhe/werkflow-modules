from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DynamoDBUpdateContributorInsightsResponse(BaseModel):
    TableName: StrictStr | None = None
    IndexName: StrictStr | None = None
    ContributorInsightsStatus: StrictStr | None = None
    ContributorInsightsMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
