from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessPersonalizationConfiguration(BaseModel):
    personalizationControlMode: StrictStr | None = None
