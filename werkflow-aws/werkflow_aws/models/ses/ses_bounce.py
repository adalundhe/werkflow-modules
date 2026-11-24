from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESBounce(BaseModel):
    BounceType: StrictStr | None = None
    BounceSubType: StrictStr | None = None
    DiagnosticCode: StrictStr | None = None
