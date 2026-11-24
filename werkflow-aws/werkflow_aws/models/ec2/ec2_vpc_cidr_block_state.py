from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VpcCidrBlockState(BaseModel):
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
