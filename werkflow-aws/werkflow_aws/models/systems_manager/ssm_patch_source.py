from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMPatchSource(BaseModel):
    Name: StrictStr | None = None
    Products: list[StrictStr] | None = None
    Configuration: StrictStr | None = None
