from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftResourcePolicy(BaseModel):
    ResourceArn: StrictStr | None = None
    Policy: StrictStr | None = None
