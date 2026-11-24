from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_reserved_instances_id import EC2ReservedInstancesId
from .ec2_reserved_instances_modification_result import EC2ReservedInstancesModificationResult


class EC2ReservedInstancesModification(BaseModel):
    ClientToken: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    EffectiveDate: datetime.datetime | StrictStr | None = None
    ModificationResults: list[EC2ReservedInstancesModificationResult] | None = None
    ReservedInstancesIds: list[EC2ReservedInstancesId] | None = None
    ReservedInstancesModificationId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    UpdateDate: datetime.datetime | StrictStr | None = None
