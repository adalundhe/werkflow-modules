from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3SSEKMS(BaseModel):
    KeyId: StrictStr | None = None
