from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessQAppsConfiguration(BaseModel):
    qAppsControlMode: StrictStr | None = None
