from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_cache_attributes import StorageGatewayCacheAttributes
from .storage_gateway_endpoint_network_configuration import StorageGatewayEndpointNetworkConfiguration
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayAssociateFileSystemRequest(BaseModel):
    UserName: StrictStr
    Password: StrictStr
    ClientToken: StrictStr
    GatewayARN: StrictStr
    LocationARN: StrictStr
    Tags: list[StorageGatewayTag] | None = None
    AuditDestinationARN: StrictStr | None = None
    CacheAttributes: StorageGatewayCacheAttributes | None = None
    EndpointNetworkConfiguration: StorageGatewayEndpointNetworkConfiguration | None = None
