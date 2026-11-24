from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_stateless_custom_action_definition import SecurityHubStatelessCustomActionDefinition


class SecurityHubRuleGroupSourceCustomActionsDetails(BaseModel):
    ActionDefinition: SecurityHubStatelessCustomActionDefinition | None = None
    ActionName: StrictStr | None = None
