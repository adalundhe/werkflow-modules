from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerProposedNetworkFunctionGroupChange(BaseModel):
    Tags: list[NetworkManagerTag] | None = None
    AttachmentPolicyRuleNumber: StrictInt | None = None
    NetworkFunctionGroupName: StrictStr | None = None
