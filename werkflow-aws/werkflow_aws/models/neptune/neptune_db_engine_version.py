from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_character_set import NeptuneCharacterSet
from .neptune_timezone import NeptuneTimezone
from .neptune_upgrade_target import NeptuneUpgradeTarget


class NeptuneDBEngineVersion(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DBParameterGroupFamily: StrictStr | None = None
    DBEngineDescription: StrictStr | None = None
    DBEngineVersionDescription: StrictStr | None = None
    DefaultCharacterSet: NeptuneCharacterSet | None = None
    SupportedCharacterSets: list[NeptuneCharacterSet] | None = None
    ValidUpgradeTarget: list[NeptuneUpgradeTarget] | None = None
    SupportedTimezones: list[NeptuneTimezone] | None = None
    ExportableLogTypes: list[StrictStr] | None = None
    SupportsLogExportsToCloudwatchLogs: StrictBool | None = None
    SupportsReadReplica: StrictBool | None = None
    SupportsGlobalDatabases: StrictBool | None = None
