from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_availability_zone_model import RDSAvailabilityZoneModel
from .rds_outpost_model import RDSOutpostModel


class RDSSubnetModel(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: RDSAvailabilityZoneModel | None = None
    SubnetOutpost: RDSOutpostModel | None = None
    SubnetStatus: StrictStr | None = None
