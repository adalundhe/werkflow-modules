from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMREc2InstanceAttributes(BaseModel):
    Ec2KeyName: StrictStr | None = None
    Ec2SubnetId: StrictStr | None = None
    RequestedEc2SubnetIds: list[StrictStr] | None = None
    Ec2AvailabilityZone: StrictStr | None = None
    RequestedEc2AvailabilityZones: list[StrictStr] | None = None
    IamInstanceProfile: StrictStr | None = None
    EmrManagedMasterSecurityGroup: StrictStr | None = None
    EmrManagedSlaveSecurityGroup: StrictStr | None = None
    ServiceAccessSecurityGroup: StrictStr | None = None
    AdditionalMasterSecurityGroups: list[StrictStr] | None = None
    AdditionalSlaveSecurityGroups: list[StrictStr] | None = None
