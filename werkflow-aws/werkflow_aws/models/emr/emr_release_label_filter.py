from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRReleaseLabelFilter(BaseModel):
    Prefix: StrictStr | None = None
    Application: StrictStr | None = None
