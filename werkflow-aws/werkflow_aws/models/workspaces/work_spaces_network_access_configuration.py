from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesNetworkAccessConfiguration(BaseModel):
    EniPrivateIpAddress: StrictStr | None = None
    EniId: StrictStr | None = None
