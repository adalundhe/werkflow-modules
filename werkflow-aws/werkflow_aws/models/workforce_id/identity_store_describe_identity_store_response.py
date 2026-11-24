from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .identity_store_network_configuration_details import IdentityStoreNetworkConfigurationDetails


class IdentityStoreDescribeIdentityStoreResponse(BaseModel):
    IdentityStoreId: StrictStr | None = None
    IdentityStoreArn: StrictStr | None = None
    NetworkConfiguration: IdentityStoreNetworkConfigurationDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
