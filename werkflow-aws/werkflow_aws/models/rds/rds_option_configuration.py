from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_option_setting import RDSOptionSetting


class RDSOptionConfiguration(BaseModel):
    OptionName: StrictStr
    Port: StrictInt | None = None
    OptionVersion: StrictStr | None = None
    DBSecurityGroupMemberships: list[StrictStr] | None = None
    VpcSecurityGroupMemberships: list[StrictStr] | None = None
    OptionSettings: list[RDSOptionSetting] | None = None
