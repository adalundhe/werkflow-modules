from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2BundleTaskError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
