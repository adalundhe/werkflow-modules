from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferUpdateWebAppIdentityCenterConfig(BaseModel):
    Role: StrictStr | None = None
