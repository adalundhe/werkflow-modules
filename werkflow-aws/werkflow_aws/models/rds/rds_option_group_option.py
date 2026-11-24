from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_option_group_option_setting import RDSOptionGroupOptionSetting
from .rds_option_version import RDSOptionVersion


class RDSOptionGroupOption(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    EngineName: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
    MinimumRequiredMinorEngineVersion: StrictStr | None = None
    PortRequired: StrictBool | None = None
    DefaultPort: StrictInt | None = None
    OptionsDependedOn: list[StrictStr] | None = None
    OptionsConflictsWith: list[StrictStr] | None = None
    Persistent: StrictBool | None = None
    Permanent: StrictBool | None = None
    RequiresAutoMinorEngineVersionUpgrade: StrictBool | None = None
    VpcOnly: StrictBool | None = None
    SupportsOptionVersionDowngrade: StrictBool | None = None
    OptionGroupOptionSettings: list[RDSOptionGroupOptionSetting] | None = None
    OptionGroupOptionVersions: list[RDSOptionVersion] | None = None
    CopyableCrossAccount: StrictBool | None = None
    CopyableCrossRegion: StrictBool | None = None
