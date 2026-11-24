from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSLakehouseSettings(BaseModel):
    Arn: StrictStr | None = None
