from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_permissions_error_context import NetworkManagerPermissionsErrorContext


class NetworkManagerPeeringError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    RequestId: StrictStr | None = None
    MissingPermissionsContext: NetworkManagerPermissionsErrorContext | None = None
