from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_available_capacity import EC2AvailableCapacity
from .ec2_host_cpu_options import EC2HostCpuOptions
from .ec2_host_instance import EC2HostInstance
from .ec2_host_properties import EC2HostProperties
from .ec2_tag_model import EC2TagModel


class EC2Host(BaseModel):
    AutoPlacement: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailableCapacity: EC2AvailableCapacity | None = None
    ClientToken: StrictStr | None = None
    HostId: StrictStr | None = None
    HostProperties: EC2HostProperties | None = None
    HostReservationId: StrictStr | None = None
    Instances: list[EC2HostInstance] | None = None
    State: StrictStr | None = None
    AllocationTime: datetime.datetime | StrictStr | None = None
    ReleaseTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    HostRecovery: StrictStr | None = None
    AllowsMultipleInstanceTypes: StrictStr | None = None
    OwnerId: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    MemberOfServiceLinkedResourceGroup: StrictBool | None = None
    OutpostArn: StrictStr | None = None
    HostMaintenance: StrictStr | None = None
    AssetId: StrictStr | None = None
    CpuOptions: EC2HostCpuOptions | None = None
