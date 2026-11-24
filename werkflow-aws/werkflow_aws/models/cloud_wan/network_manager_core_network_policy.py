from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .network_manager_core_network_policy_error import NetworkManagerCoreNetworkPolicyError


class NetworkManagerCoreNetworkPolicy(BaseModel):
    CoreNetworkId: StrictStr | None = None
    PolicyVersionId: StrictInt | None = None
    Alias: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ChangeSetState: StrictStr | None = None
    PolicyErrors: list[NetworkManagerCoreNetworkPolicyError] | None = None
    PolicyDocument: StrictStr | None = None
