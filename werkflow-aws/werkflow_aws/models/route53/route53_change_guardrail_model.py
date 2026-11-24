from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ChangeGuardrailModel(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
