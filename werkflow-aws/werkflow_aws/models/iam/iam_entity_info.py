from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMEntityInfo(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Id: StrictStr | None = None
    Path: StrictStr | None = None
