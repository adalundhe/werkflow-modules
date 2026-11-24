from __future__ import annotations
from pydantic import BaseModel
from .directory_service_hybrid_update_info_entry import DirectoryServiceHybridUpdateInfoEntry


class DirectoryServiceHybridUpdateActivities(BaseModel):
    SelfManagedInstances: list[DirectoryServiceHybridUpdateInfoEntry] | None = None
    HybridAdministratorAccount: list[DirectoryServiceHybridUpdateInfoEntry] | None = None
