from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_client_side_action_config import WAFv2ClientSideActionConfig


class WAFv2AWSManagedRulesAntiDDoSRuleSet(BaseModel):
    ClientSideActionConfig: WAFv2ClientSideActionConfig | None = None
    SensitivityToBlock: StrictStr | None = None
