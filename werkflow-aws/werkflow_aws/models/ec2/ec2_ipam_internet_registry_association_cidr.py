from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2IpamInternetRegistryAssociationCidr(BaseModel):
    Cidr: StrictStr | None = None
    LastObservedAt: datetime.datetime | StrictStr | None = None
