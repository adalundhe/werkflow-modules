from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESTenantSuppressionAttributes(BaseModel):
    SuppressedReasons: list[StrictStr] | None = None
    SuppressionScope: StrictStr | None = None
