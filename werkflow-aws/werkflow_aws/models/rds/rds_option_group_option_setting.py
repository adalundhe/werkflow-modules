from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_minimum_engine_version_per_allowed_value import RDSMinimumEngineVersionPerAllowedValue


class RDSOptionGroupOptionSetting(BaseModel):
    SettingName: StrictStr | None = None
    SettingDescription: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    ApplyType: StrictStr | None = None
    AllowedValues: StrictStr | None = None
    IsModifiable: StrictBool | None = None
    IsRequired: StrictBool | None = None
    MinimumEngineVersionPerAllowedValue: list[RDSMinimumEngineVersionPerAllowedValue] | None = None
