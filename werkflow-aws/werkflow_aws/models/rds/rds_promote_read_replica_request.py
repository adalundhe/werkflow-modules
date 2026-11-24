from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_tag_specification_model import RDSTagSpecificationModel


class RDSPromoteReadReplicaRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    TagSpecifications: list[RDSTagSpecificationModel] | None = None
