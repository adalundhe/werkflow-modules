from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .direct_connect_mac_sec_key import DirectConnectMacSecKey
from .direct_connect_rate_limiter_status import DirectConnectRateLimiterStatus
from .direct_connect_tag import DirectConnectTag


class DirectConnectAssociateHostedConnectionResponse(BaseModel):
    ownerAccount: StrictStr | None = None
    connectionId: StrictStr | None = None
    connectionName: StrictStr | None = None
    connectionState: StrictStr | None = None
    region: StrictStr | None = None
    location: StrictStr | None = None
    bandwidth: StrictStr | None = None
    vlan: StrictInt | None = None
    partnerName: StrictStr | None = None
    loaIssueTime: datetime.datetime | StrictStr | None = None
    lagId: StrictStr | None = None
    awsDevice: StrictStr | None = None
    jumboFrameCapable: StrictBool | None = None
    awsDeviceV2: StrictStr | None = None
    awsLogicalDeviceId: StrictStr | None = None
    hasLogicalRedundancy: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    providerName: StrictStr | None = None
    macSecCapable: StrictBool | None = None
    portEncryptionStatus: StrictStr | None = None
    encryptionMode: StrictStr | None = None
    macSecKeys: list[DirectConnectMacSecKey] | None = None
    rateLimiterStatus: DirectConnectRateLimiterStatus | None = None
    partnerInterconnectMacSecCapable: StrictBool | None = None
    prefixPoolSizeIpv4: StrictInt | None = None
    prefixPoolSizeIpv6: StrictInt | None = None
    prefixPoolUnallocatedCountIpv4: StrictInt | None = None
    prefixPoolUnallocatedCountIpv6: StrictInt | None = None
    billingMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
