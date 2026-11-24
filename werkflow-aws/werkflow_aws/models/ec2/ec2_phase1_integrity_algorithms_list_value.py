from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Phase1IntegrityAlgorithmsListValue(BaseModel):
    Value: StrictStr | None = None
