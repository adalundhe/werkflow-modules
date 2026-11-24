from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2IpamRouteOriginAuthorization(BaseModel):
    Asn: StrictStr | None = None
    Prefix: StrictStr | None = None
    MaxLength: StrictInt | None = None
    Match: StrictBool | None = None
    Expiration: datetime.datetime | StrictStr | None = None
