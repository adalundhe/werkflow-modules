from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribedIdentityCenterConfig(BaseModel):
    ApplicationArn: StrictStr | None = None
    InstanceArn: StrictStr | None = None
    Role: StrictStr | None = None
