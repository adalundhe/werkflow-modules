from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_option_configuration import RDSOptionConfiguration


class RDSModifyOptionGroupRequest(BaseModel):
    OptionGroupName: StrictStr
    OptionsToInclude: list[RDSOptionConfiguration] | None = None
    OptionsToRemove: list[StrictStr] | None = None
    ApplyImmediately: StrictBool | None = None
