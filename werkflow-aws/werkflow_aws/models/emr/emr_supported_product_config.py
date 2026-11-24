from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRSupportedProductConfig(BaseModel):
    Name: StrictStr | None = None
    Args: list[StrictStr] | None = None
