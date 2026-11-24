from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_tag_model import RDSTagModel


class RDSPurchaseReservedDBInstancesOfferingRequest(BaseModel):
    ReservedDBInstancesOfferingId: StrictStr
    ReservedDBInstanceId: StrictStr | None = None
    DBInstanceCount: StrictInt | None = None
    Tags: list[RDSTagModel] | None = None
