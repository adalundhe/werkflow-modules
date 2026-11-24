from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSOptionVersion(BaseModel):
    Version: StrictStr | None = None
    IsDefault: StrictBool | None = None
