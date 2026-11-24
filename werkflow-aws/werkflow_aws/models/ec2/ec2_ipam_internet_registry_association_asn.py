from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2IpamInternetRegistryAssociationAsn(BaseModel):
    Asn: StrictStr | None = None
    LastObservedAt: datetime.datetime | StrictStr | None = None
