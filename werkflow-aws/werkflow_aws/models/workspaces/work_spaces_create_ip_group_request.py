from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_ip_rule_item import WorkSpacesIpRuleItem
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesCreateIpGroupRequest(BaseModel):
    GroupName: StrictStr
    GroupDesc: StrictStr | None = None
    UserRules: list[WorkSpacesIpRuleItem] | None = None
    Tags: list[WorkSpacesTag] | None = None
