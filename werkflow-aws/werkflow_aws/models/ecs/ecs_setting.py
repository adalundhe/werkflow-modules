from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSSetting(BaseModel):
    name: StrictStr | None = None
    value: StrictStr | None = None
    principalArn: StrictStr | None = None
    type: StrictStr | None = None
