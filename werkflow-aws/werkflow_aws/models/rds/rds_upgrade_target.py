from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSUpgradeTarget(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Description: StrictStr | None = None
    AutoUpgrade: StrictBool | None = None
    IsMajorVersionUpgrade: StrictBool | None = None
    SupportedEngineModes: list[StrictStr] | None = None
    SupportsParallelQuery: StrictBool | None = None
    SupportsGlobalDatabases: StrictBool | None = None
    SupportsBabelfish: StrictBool | None = None
    SupportsLimitlessDatabase: StrictBool | None = None
    SupportsLocalWriteForwarding: StrictBool | None = None
    SupportsIntegrations: StrictBool | None = None
