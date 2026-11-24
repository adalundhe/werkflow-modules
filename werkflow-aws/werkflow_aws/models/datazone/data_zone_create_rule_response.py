from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_rule_detail import DataZoneRuleDetail
from .data_zone_rule_scope import DataZoneRuleScope
from .data_zone_rule_target import DataZoneRuleTarget


class DataZoneCreateRuleResponse(BaseModel):
    identifier: StrictStr | None = None
    name: StrictStr | None = None
    ruleType: StrictStr | None = None
    target: DataZoneRuleTarget | None = None
    action: StrictStr | None = None
    scope: DataZoneRuleScope | None = None
    detail: DataZoneRuleDetail | None = None
    targetType: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
