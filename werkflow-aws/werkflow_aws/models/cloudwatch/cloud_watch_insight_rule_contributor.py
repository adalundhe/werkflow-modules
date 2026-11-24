from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .cloud_watch_insight_rule_contributor_datapoint import CloudWatchInsightRuleContributorDatapoint


class CloudWatchInsightRuleContributor(BaseModel):
    Keys: list[StrictStr] | None = None
    ApproximateAggregateValue: StrictFloat | StrictInt | None = None
    Datapoints: list[CloudWatchInsightRuleContributorDatapoint] | None = None
