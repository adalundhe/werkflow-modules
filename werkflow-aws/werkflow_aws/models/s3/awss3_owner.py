from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3Owner(BaseModel):
    DisplayName: StrictStr | None = None
    ID: StrictStr | None = None
