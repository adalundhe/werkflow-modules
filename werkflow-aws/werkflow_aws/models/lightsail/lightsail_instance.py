from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_add_on import LightsailAddOn
from .lightsail_instance_hardware import LightsailInstanceHardware
from .lightsail_instance_health_status import LightsailInstanceHealthStatus
from .lightsail_instance_metadata_options import LightsailInstanceMetadataOptions
from .lightsail_instance_networking import LightsailInstanceNetworking
from .lightsail_instance_state import LightsailInstanceState
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailInstance(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    blueprintId: StrictStr | None = None
    blueprintName: StrictStr | None = None
    bundleId: StrictStr | None = None
    addOns: list[LightsailAddOn] | None = None
    isStaticIp: StrictBool | None = None
    privateIpAddress: StrictStr | None = None
    publicIpAddress: StrictStr | None = None
    ipv6Addresses: list[StrictStr] | None = None
    ipAddressType: StrictStr | None = None
    hardware: LightsailInstanceHardware | None = None
    networking: LightsailInstanceNetworking | None = None
    state: LightsailInstanceState | None = None
    username: StrictStr | None = None
    sshKeyName: StrictStr | None = None
    metadataOptions: LightsailInstanceMetadataOptions | None = None
    instanceStatus: LightsailInstanceHealthStatus | None = None
    systemStatus: LightsailInstanceHealthStatus | None = None
