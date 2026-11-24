from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxS3AccessPointVpcConfiguration(BaseModel):
    VpcId: StrictStr | None = None
