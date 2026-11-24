from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAwsConsoleLinkParameters(BaseModel):
    uri: StrictStr | None = None
