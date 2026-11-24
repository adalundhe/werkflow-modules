from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListServerCertificateTagsRequest(BaseModel):
    ServerCertificateName: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
