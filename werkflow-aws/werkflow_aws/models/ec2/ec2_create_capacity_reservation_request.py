from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateCapacityReservationRequest(BaseModel):
    InstanceType: StrictStr
    InstancePlatform: Literal['Linux/UNIX', 'Red Hat Enterprise Linux', 'SUSE Linux', 'Windows', 'Windows with SQL Server', 'Windows with SQL Server Enterprise', 'Windows with SQL Server Standard', 'Windows with SQL Server Web', 'Linux with SQL Server Standard', 'Linux with SQL Server Web', 'Linux with SQL Server Enterprise', 'RHEL with SQL Server Standard', 'RHEL with SQL Server Enterprise', 'RHEL with SQL Server Web', 'RHEL with HA', 'RHEL with HA and SQL Server Standard', 'RHEL with HA and SQL Server Enterprise', 'Ubuntu Pro']
    InstanceCount: StrictInt
    ClientToken: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Tenancy: Literal['default', 'dedicated'] | None = None
    EbsOptimized: StrictBool | None = None
    EphemeralStorage: StrictBool | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    EndDateType: Literal['unlimited', 'limited'] | None = None
    InstanceMatchCriteria: Literal['open', 'targeted'] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
    OutpostArn: StrictStr | None = None
    PlacementGroupArn: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    CommitmentDuration: StrictInt | None = None
    DeliveryPreference: Literal['fixed', 'incremental'] | None = None
