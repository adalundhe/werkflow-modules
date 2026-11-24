from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ProductCode(BaseModel):
    ProductCodeId: StrictStr | None = None
    ProductCodeType: StrictStr | None = None
