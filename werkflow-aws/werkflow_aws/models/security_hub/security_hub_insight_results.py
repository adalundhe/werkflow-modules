from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_insight_result_value import SecurityHubInsightResultValue


class SecurityHubInsightResults(BaseModel):
    InsightArn: StrictStr | None = None
    GroupByAttribute: StrictStr | None = None
    ResultValues: list[SecurityHubInsightResultValue] | None = None
