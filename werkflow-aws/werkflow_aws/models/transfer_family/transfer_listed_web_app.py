from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferListedWebApp(BaseModel):
    Arn: StrictStr | None = None
    WebAppId: StrictStr | None = None
    AccessEndpoint: StrictStr | None = None
    WebAppEndpoint: StrictStr | None = None
    EndpointType: StrictStr | None = None
