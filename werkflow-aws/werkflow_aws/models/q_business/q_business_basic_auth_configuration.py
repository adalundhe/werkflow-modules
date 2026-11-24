from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessBasicAuthConfiguration(BaseModel):
    secretArn: StrictStr | None = None
    roleArn: StrictStr | None = None
