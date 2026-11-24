from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_rule_configuration import QBusinessRuleConfiguration
from .q_business_users_and_groups import QBusinessUsersAndGroups


class QBusinessRule(BaseModel):
    includedUsersAndGroups: QBusinessUsersAndGroups | None = None
    excludedUsersAndGroups: QBusinessUsersAndGroups | None = None
    ruleType: StrictStr | None = None
    ruleConfiguration: QBusinessRuleConfiguration | None = None
