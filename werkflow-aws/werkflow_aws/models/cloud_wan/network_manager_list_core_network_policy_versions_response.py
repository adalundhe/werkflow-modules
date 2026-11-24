from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_policy_version import NetworkManagerCoreNetworkPolicyVersion


class NetworkManagerListCoreNetworkPolicyVersionsResponse(BaseModel):
    CoreNetworkPolicyVersions: list[NetworkManagerCoreNetworkPolicyVersion] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
