from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferIdentityCenterConfig(BaseModel):
    InstanceArn: StrictStr | None = None
    Role: StrictStr | None = None
