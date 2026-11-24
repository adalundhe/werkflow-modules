from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_rule_detail import DataZoneRuleDetail
from .data_zone_rule_scope import DataZoneRuleScope
from .data_zone_rule_target import DataZoneRuleTarget


class DataZoneCreateRuleRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    target: DataZoneRuleTarget
    action: Literal['CREATE_LISTING_CHANGE_SET', 'CREATE_SUBSCRIPTION_REQUEST']
    scope: DataZoneRuleScope
    detail: DataZoneRuleDetail
    description: StrictStr | None = None
    clientToken: StrictStr | None = None
