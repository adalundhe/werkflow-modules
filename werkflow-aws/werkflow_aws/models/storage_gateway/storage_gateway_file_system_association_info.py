from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_cache_attributes import StorageGatewayCacheAttributes
from .storage_gateway_endpoint_network_configuration import StorageGatewayEndpointNetworkConfiguration
from .storage_gateway_file_system_association_status_detail import StorageGatewayFileSystemAssociationStatusDetail
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayFileSystemAssociationInfo(BaseModel):
    FileSystemAssociationARN: StrictStr | None = None
    LocationARN: StrictStr | None = None
    FileSystemAssociationStatus: StrictStr | None = None
    AuditDestinationARN: StrictStr | None = None
    GatewayARN: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
    CacheAttributes: StorageGatewayCacheAttributes | None = None
    EndpointNetworkConfiguration: StorageGatewayEndpointNetworkConfiguration | None = None
    FileSystemAssociationStatusDetails: list[StorageGatewayFileSystemAssociationStatusDetail] | None = None
