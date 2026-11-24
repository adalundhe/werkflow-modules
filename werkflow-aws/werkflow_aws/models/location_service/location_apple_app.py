from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationAppleApp(BaseModel):
    BundleId: StrictStr | None = None
