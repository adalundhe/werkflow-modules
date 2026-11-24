from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2VgwTelemetry(BaseModel):
    AcceptedRouteCount: StrictInt | None = None
    LastStatusChange: datetime.datetime | StrictStr | None = None
    OutsideIpAddress: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CertificateArn: StrictStr | None = None
