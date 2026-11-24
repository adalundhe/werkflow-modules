from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchPutInsightRuleRequest(BaseModel):
    RuleName: StrictStr
    RuleDefinition: StrictStr
    RuleState: StrictStr | None = None
    Tags: list[CloudWatchTagModel] | None = None
    ApplyOnTransformedLogs: StrictBool | None = None
