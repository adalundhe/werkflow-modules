from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_managed_rule_state import CloudWatchManagedRuleState


class CloudWatchManagedRuleDescription(BaseModel):
    TemplateName: StrictStr | None = None
    ResourceARN: StrictStr | None = None
    RuleState: CloudWatchManagedRuleState | None = None
