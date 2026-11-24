from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_sub_slot_value_elicitation_setting import LexSubSlotValueElicitationSetting


class LexSpecifications(BaseModel):
    slotTypeId: StrictStr | None = None
    valueElicitationSetting: LexSubSlotValueElicitationSetting | None = None
