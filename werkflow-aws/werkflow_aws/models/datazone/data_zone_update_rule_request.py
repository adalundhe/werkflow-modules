from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_rule_detail import DataZoneRuleDetail
from .data_zone_rule_scope import DataZoneRuleScope


class DataZoneUpdateRuleRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    scope: DataZoneRuleScope | None = None
    detail: DataZoneRuleDetail | None = None
    includeChildDomainUnits: StrictBool | None = None
