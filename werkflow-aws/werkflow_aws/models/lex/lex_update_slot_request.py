from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_multiple_values_setting import LexMultipleValuesSetting
from .lex_obfuscation_setting import LexObfuscationSetting
from .lex_slot_value_elicitation_setting import LexSlotValueElicitationSetting
from .lex_sub_slot_setting import LexSubSlotSetting


class LexUpdateSlotRequest(BaseModel):
    slotId: StrictStr
    slotName: StrictStr
    valueElicitationSetting: LexSlotValueElicitationSetting
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    intentId: StrictStr
    description: StrictStr | None = None
    slotTypeId: StrictStr | None = None
    obfuscationSetting: LexObfuscationSetting | None = None
    multipleValuesSetting: LexMultipleValuesSetting | None = None
    subSlotSetting: LexSubSlotSetting | None = None
