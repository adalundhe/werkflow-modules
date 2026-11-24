from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_ebs_volume import EMREbsVolume
from .emr_instance_status import EMRInstanceStatus


class EMRInstance(BaseModel):
    Id: StrictStr | None = None
    Ec2InstanceId: StrictStr | None = None
    PublicDnsName: StrictStr | None = None
    PublicIpAddress: StrictStr | None = None
    PrivateDnsName: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    Status: EMRInstanceStatus | None = None
    InstanceGroupId: StrictStr | None = None
    InstanceFleetId: StrictStr | None = None
    Market: StrictStr | None = None
    InstanceType: StrictStr | None = None
    EbsVolumes: list[EMREbsVolume] | None = None
