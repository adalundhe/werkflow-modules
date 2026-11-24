from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFDomainInfo(BaseModel):
    name: StrictStr | None = None
    status: StrictStr | None = None
    description: StrictStr | None = None
    arn: StrictStr | None = None
