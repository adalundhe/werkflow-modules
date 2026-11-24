from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessHallucinationReductionConfiguration(BaseModel):
    hallucinationReductionControl: StrictStr | None = None
