from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    SourceDBClusterIdentifier: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    DatabaseName: StrictStr | None = None
    Tags: list[NeptuneTag] | None = None
    StorageEncrypted: StrictBool | None = None
