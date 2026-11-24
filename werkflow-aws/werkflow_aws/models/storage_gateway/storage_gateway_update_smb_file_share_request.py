from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .storage_gateway_cache_attributes import StorageGatewayCacheAttributes


class StorageGatewayUpdateSMBFileShareRequest(BaseModel):
    FileShareARN: StrictStr
    EncryptionType: Literal['SseS3', 'SseKms', 'DsseKms'] | None = None
    KMSEncrypted: StrictBool | None = None
    KMSKey: StrictStr | None = None
    DefaultStorageClass: StrictStr | None = None
    ObjectACL: Literal['private', 'public-read', 'public-read-write', 'authenticated-read', 'bucket-owner-read', 'bucket-owner-full-control', 'aws-exec-read'] | None = None
    ReadOnly: StrictBool | None = None
    GuessMIMETypeEnabled: StrictBool | None = None
    RequesterPays: StrictBool | None = None
    SMBACLEnabled: StrictBool | None = None
    AccessBasedEnumeration: StrictBool | None = None
    AdminUserList: list[StrictStr] | None = None
    ValidUserList: list[StrictStr] | None = None
    InvalidUserList: list[StrictStr] | None = None
    AuditDestinationARN: StrictStr | None = None
    CaseSensitivity: Literal['ClientSpecified', 'CaseSensitive'] | None = None
    FileShareName: StrictStr | None = None
    CacheAttributes: StorageGatewayCacheAttributes | None = None
    NotificationPolicy: StrictStr | None = None
    OplocksEnabled: StrictBool | None = None
