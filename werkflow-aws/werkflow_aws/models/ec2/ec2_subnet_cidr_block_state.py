from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SubnetCidrBlockState(BaseModel):
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
