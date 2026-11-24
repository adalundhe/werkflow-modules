from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListServerCertificatesRequest(BaseModel):
    PathPrefix: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
