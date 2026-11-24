from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .wa_fv2_field_to_protect import WAFv2FieldToProtect


class WAFv2DataProtection(BaseModel):
    Field: WAFv2FieldToProtect | None = None
    Action: StrictStr | None = None
    ExcludeRuleMatchDetails: StrictBool | None = None
    ExcludeRateBasedDetails: StrictBool | None = None
