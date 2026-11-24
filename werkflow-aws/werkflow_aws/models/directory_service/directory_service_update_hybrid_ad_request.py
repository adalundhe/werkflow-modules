from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_hybrid_administrator_account_update import DirectoryServiceHybridAdministratorAccountUpdate
from .directory_service_hybrid_customer_instances_settings import DirectoryServiceHybridCustomerInstancesSettings


class DirectoryServiceUpdateHybridADRequest(BaseModel):
    DirectoryId: StrictStr
    HybridAdministratorAccountUpdate: DirectoryServiceHybridAdministratorAccountUpdate | None = None
    SelfManagedInstancesSettings: DirectoryServiceHybridCustomerInstancesSettings | None = None
