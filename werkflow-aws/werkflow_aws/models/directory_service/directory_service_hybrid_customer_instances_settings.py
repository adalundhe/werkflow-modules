from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceHybridCustomerInstancesSettings(BaseModel):
    CustomerDnsIps: list[StrictStr]
    InstanceIds: list[StrictStr]
