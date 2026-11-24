from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessIdcAuthConfiguration(BaseModel):
    idcApplicationArn: StrictStr | None = None
    roleArn: StrictStr | None = None
