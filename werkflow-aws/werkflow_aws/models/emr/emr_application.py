from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRApplication(BaseModel):
    Name: StrictStr | None = None
    Version: StrictStr | None = None
    Args: list[StrictStr] | None = None
    AdditionalInfo: dict[StrictStr, StrictStr] | None = None
