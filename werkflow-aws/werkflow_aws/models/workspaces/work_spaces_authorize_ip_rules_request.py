from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_ip_rule_item import WorkSpacesIpRuleItem


class WorkSpacesAuthorizeIpRulesRequest(BaseModel):
    GroupId: StrictStr
    UserRules: list[WorkSpacesIpRuleItem]
