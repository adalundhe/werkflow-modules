from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_network_interface import StorageGatewayNetworkInterface
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayDescribeGatewayInformationResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    GatewayId: StrictStr | None = None
    GatewayName: StrictStr | None = None
    GatewayTimezone: StrictStr | None = None
    GatewayState: StrictStr | None = None
    GatewayNetworkInterfaces: list[StorageGatewayNetworkInterface] | None = None
    GatewayType: StrictStr | None = None
    NextUpdateAvailabilityDate: StrictStr | None = None
    LastSoftwareUpdate: StrictStr | None = None
    Ec2InstanceId: StrictStr | None = None
    Ec2InstanceRegion: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
    VPCEndpoint: StrictStr | None = None
    CloudWatchLogGroupARN: StrictStr | None = None
    HostEnvironment: StrictStr | None = None
    EndpointType: StrictStr | None = None
    SoftwareUpdatesEndDate: StrictStr | None = None
    DeprecationDate: StrictStr | None = None
    GatewayCapacity: StrictStr | None = None
    SupportedGatewayCapacities: list[StrictStr] | None = None
    HostEnvironmentId: StrictStr | None = None
    SoftwareVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
