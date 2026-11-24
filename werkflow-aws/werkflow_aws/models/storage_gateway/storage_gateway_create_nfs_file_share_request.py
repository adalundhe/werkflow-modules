from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .storage_gateway_cache_attributes import StorageGatewayCacheAttributes
from .storage_gateway_nfs_file_share_defaults import StorageGatewayNFSFileShareDefaults
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCreateNFSFileShareRequest(BaseModel):
    ClientToken: StrictStr
    GatewayARN: StrictStr
    Role: StrictStr
    LocationARN: StrictStr
    NFSFileShareDefaults: StorageGatewayNFSFileShareDefaults | None = None
    EncryptionType: Literal['SseS3', 'SseKms', 'DsseKms'] | None = None
    KMSEncrypted: StrictBool | None = None
    KMSKey: StrictStr | None = None
    DefaultStorageClass: StrictStr | None = None
    ObjectACL: Literal['private', 'public-read', 'public-read-write', 'authenticated-read', 'bucket-owner-read', 'bucket-owner-full-control', 'aws-exec-read'] | None = None
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
