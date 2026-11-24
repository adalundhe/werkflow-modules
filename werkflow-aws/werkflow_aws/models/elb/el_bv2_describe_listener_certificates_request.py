from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeListenerCertificatesRequest(BaseModel):
    ListenerArn: StrictStr
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
