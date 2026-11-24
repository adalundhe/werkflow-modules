from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_availability_zone import RedshiftAvailabilityZone


class RedshiftOrderableClusterOption(BaseModel):
    ClusterVersion: StrictStr | None = None
    ClusterType: StrictStr | None = None
    NodeType: StrictStr | None = None
    AvailabilityZones: list[RedshiftAvailabilityZone] | None = None
