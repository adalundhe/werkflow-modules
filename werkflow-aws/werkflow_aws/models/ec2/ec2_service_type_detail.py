from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ServiceTypeDetail(BaseModel):
    ServiceType: StrictStr | None = None
