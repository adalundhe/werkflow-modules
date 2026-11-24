from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateKmsKeyIdRequest(BaseModel):
    KmsKeyId: StrictStr
    SnapshotId: StrictStr | None = None
    DryRun: StrictBool | None = None
