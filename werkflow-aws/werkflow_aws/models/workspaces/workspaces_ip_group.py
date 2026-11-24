from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_ip_rule_item import WorkSpacesIpRuleItem


class WorkspacesIpGroup(BaseModel):
    groupId: StrictStr | None = None
    groupName: StrictStr | None = None
    groupDesc: StrictStr | None = None
    userRules: list[WorkSpacesIpRuleItem] | None = None
