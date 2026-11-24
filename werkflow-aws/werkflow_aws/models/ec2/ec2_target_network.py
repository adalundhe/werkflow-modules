from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_association_status import EC2AssociationStatus


class EC2TargetNetwork(BaseModel):
    AssociationId: StrictStr | None = None
    VpcId: StrictStr | None = None
    TargetNetworkId: StrictStr | None = None
    ClientVpnEndpointId: StrictStr | None = None
    Status: EC2AssociationStatus | None = None
    SecurityGroups: list[StrictStr] | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
