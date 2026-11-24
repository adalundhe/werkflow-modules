from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_availability_zone import RDSAvailabilityZone
from .rds_outpost import RDSOutpost


class RDSSubnet(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: RDSAvailabilityZone | None = None
    SubnetOutpost: RDSOutpost | None = None
    SubnetStatus: StrictStr | None = None
