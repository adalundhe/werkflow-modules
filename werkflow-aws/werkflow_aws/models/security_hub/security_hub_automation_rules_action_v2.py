from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_automation_rules_finding_fields_update_v2 import SecurityHubAutomationRulesFindingFieldsUpdateV2
from .security_hub_automation_rules_resource_fields_update_v2 import SecurityHubAutomationRulesResourceFieldsUpdateV2
from .security_hub_external_integration_configuration import SecurityHubExternalIntegrationConfiguration


class SecurityHubAutomationRulesActionV2(BaseModel):
    Type: StrictStr | None = None
    FindingFieldsUpdate: SecurityHubAutomationRulesFindingFieldsUpdateV2 | None = None
    ExternalIntegrationConfiguration: SecurityHubExternalIntegrationConfiguration | None = None
    ResourceFieldsUpdate: SecurityHubAutomationRulesResourceFieldsUpdateV2 | None = None
