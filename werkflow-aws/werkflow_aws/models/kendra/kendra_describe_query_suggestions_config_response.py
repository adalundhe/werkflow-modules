from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .kendra_attribute_suggestions_describe_config import KendraAttributeSuggestionsDescribeConfig


class KendraDescribeQuerySuggestionsConfigResponse(BaseModel):
    Mode: StrictStr | None = None
    Status: StrictStr | None = None
    QueryLogLookBackWindowInDays: StrictInt | None = None
    IncludeQueriesWithoutUserInformation: StrictBool | None = None
    MinimumNumberOfQueryingUsers: StrictInt | None = None
    MinimumQueryCount: StrictInt | None = None
    LastSuggestionsBuildTime: datetime.datetime | StrictStr | None = None
    LastClearTime: datetime.datetime | StrictStr | None = None
    TotalSuggestionsCount: StrictInt | None = None
    AttributeSuggestionsConfig: KendraAttributeSuggestionsDescribeConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
