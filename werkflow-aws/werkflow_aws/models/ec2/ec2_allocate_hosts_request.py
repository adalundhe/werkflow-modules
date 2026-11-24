from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_host_cpu_options_request import EC2HostCpuOptionsRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2AllocateHostsRequest(BaseModel):
    InstanceFamily: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    HostRecovery: Literal['on', 'off'] | None = None
    OutpostArn: StrictStr | None = None
    HostMaintenance: Literal['on', 'off'] | None = None
    AssetIds: list[StrictStr] | None = None
    AvailabilityZoneId: StrictStr | None = None
    CpuOptions: EC2HostCpuOptionsRequest | None = None
    AutoPlacement: Literal['on', 'off'] | None = None
    ClientToken: StrictStr | None = None
    InstanceType: StrictStr | None = None
    Quantity: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
