from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2UserData(BaseModel):
    Data: StrictStr | None = None
