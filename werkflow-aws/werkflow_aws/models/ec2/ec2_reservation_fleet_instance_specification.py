from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class EC2ReservationFleetInstanceSpecification(BaseModel):
    InstanceType: StrictStr | None = None
    InstancePlatform: Literal['Linux/UNIX', 'Red Hat Enterprise Linux', 'SUSE Linux', 'Windows', 'Windows with SQL Server', 'Windows with SQL Server Enterprise', 'Windows with SQL Server Standard', 'Windows with SQL Server Web', 'Linux with SQL Server Standard', 'Linux with SQL Server Web', 'Linux with SQL Server Enterprise', 'RHEL with SQL Server Standard', 'RHEL with SQL Server Enterprise', 'RHEL with SQL Server Web', 'RHEL with HA', 'RHEL with HA and SQL Server Standard', 'RHEL with HA and SQL Server Enterprise', 'Ubuntu Pro'] | None = None
    Weight: StrictFloat | StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    EbsOptimized: StrictBool | None = None
    Priority: StrictInt | None = None
