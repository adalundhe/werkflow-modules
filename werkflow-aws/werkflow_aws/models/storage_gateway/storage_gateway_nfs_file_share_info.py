from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .storage_gateway_cache_attributes import StorageGatewayCacheAttributes
from .storage_gateway_nfs_file_share_defaults import StorageGatewayNFSFileShareDefaults
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayNFSFileShareInfo(BaseModel):
    NFSFileShareDefaults: StorageGatewayNFSFileShareDefaults | None = None
    FileShareARN: StrictStr | None = None
    FileShareId: StrictStr | None = None
    FileShareStatus: StrictStr | None = None
    GatewayARN: StrictStr | None = None
    EncryptionType: StrictStr | None = None
    KMSEncrypted: StrictBool | None = None
    KMSKey: StrictStr | None = None
    Path: StrictStr | None = None
    Role: StrictStr | None = None
    LocationARN: StrictStr | None = None
    DefaultStorageClass: StrictStr | None = None
    ObjectACL: StrictStr | None = None
    ClientList: list[StrictStr] | None = None
    Squash: StrictStr | None = None
    ReadOnly: StrictBool | None = None
    GuessMIMETypeEnabled: StrictBool | None = None
    RequesterPays: StrictBool | None = None
    Tags: list[StorageGatewayTag] | None = None
    FileShareName: StrictStr | None = None
    CacheAttributes: StorageGatewayCacheAttributes | None = None
    NotificationPolicy: StrictStr | None = None
    VPCEndpointDNSName: StrictStr | None = None
    BucketRegion: StrictStr | None = None
    AuditDestinationARN: StrictStr | None = None
