from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_availability_zone import RedshiftAvailabilityZone


class RedshiftSubnet(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: RedshiftAvailabilityZone | None = None
    SubnetStatus: StrictStr | None = None
