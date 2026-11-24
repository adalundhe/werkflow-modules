from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .direct_connect_connection import DirectConnectConnection
from .direct_connect_mac_sec_key import DirectConnectMacSecKey
from .direct_connect_rate_limiter_status import DirectConnectRateLimiterStatus
from .direct_connect_tag import DirectConnectTag


class DirectConnectDeleteLagResponse(BaseModel):
    connectionsBandwidth: StrictStr | None = None
    numberOfConnections: StrictInt | None = None
    lagId: StrictStr | None = None
    ownerAccount: StrictStr | None = None
    lagName: StrictStr | None = None
    lagState: StrictStr | None = None
    location: StrictStr | None = None
    region: StrictStr | None = None
    minimumLinks: StrictInt | None = None
    awsDevice: StrictStr | None = None
    awsDeviceV2: StrictStr | None = None
    awsLogicalDeviceId: StrictStr | None = None
    connections: list[DirectConnectConnection] | None = None
    allowsHostedConnections: StrictBool | None = None
    jumboFrameCapable: StrictBool | None = None
    hasLogicalRedundancy: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    providerName: StrictStr | None = None
    macSecCapable: StrictBool | None = None
    encryptionMode: StrictStr | None = None
    macSecKeys: list[DirectConnectMacSecKey] | None = None
    prefixPoolSizeIpv4: StrictInt | None = None
    prefixPoolSizeIpv6: StrictInt | None = None
    prefixPoolUnallocatedCountIpv4: StrictInt | None = None
    prefixPoolUnallocatedCountIpv6: StrictInt | None = None
    rateLimiterStatus: DirectConnectRateLimiterStatus | None = None
    billingMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
