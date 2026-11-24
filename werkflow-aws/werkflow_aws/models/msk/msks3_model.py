from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKS3Model(BaseModel):
    Bucket: StrictStr | None = None
    Enabled: StrictBool | None = None
    Prefix: StrictStr | None = None
