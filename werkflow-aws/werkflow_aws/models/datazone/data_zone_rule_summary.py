from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_rule_scope import DataZoneRuleScope
from .data_zone_rule_target import DataZoneRuleTarget


class DataZoneRuleSummary(BaseModel):
    identifier: StrictStr | None = None
    revision: StrictStr | None = None
    ruleType: StrictStr | None = None
    name: StrictStr | None = None
    targetType: StrictStr | None = None
    target: DataZoneRuleTarget | None = None
    action: StrictStr | None = None
    scope: DataZoneRuleScope | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
