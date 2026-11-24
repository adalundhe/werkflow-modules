from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_failure_exception import DynamoDBFailureException


class DynamoDBDescribeContributorInsightsResponse(BaseModel):
    TableName: StrictStr | None = None
    IndexName: StrictStr | None = None
    ContributorInsightsRuleList: list[StrictStr] | None = None
    ContributorInsightsStatus: StrictStr | None = None
    LastUpdateDateTime: datetime.datetime | StrictStr | None = None
    FailureException: DynamoDBFailureException | None = None
    ContributorInsightsMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
