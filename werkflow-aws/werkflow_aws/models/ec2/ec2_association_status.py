from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AssociationStatus(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
