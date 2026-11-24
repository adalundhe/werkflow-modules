from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InstanceStateModel(BaseModel):
    Code: StrictInt | None = None
    Name: StrictStr | None = None
