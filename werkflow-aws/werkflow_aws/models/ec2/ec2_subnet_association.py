from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SubnetAssociation(BaseModel):
    SubnetId: StrictStr | None = None
    State: StrictStr | None = None
