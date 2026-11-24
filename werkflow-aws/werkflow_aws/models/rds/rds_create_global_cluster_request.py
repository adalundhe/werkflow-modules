from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    SourceDBClusterIdentifier: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    EngineLifecycleSupport: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    DatabaseName: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
