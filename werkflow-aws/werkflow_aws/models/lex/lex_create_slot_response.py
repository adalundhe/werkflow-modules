from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_multiple_values_setting import LexMultipleValuesSetting
from .lex_obfuscation_setting import LexObfuscationSetting
from .lex_slot_value_elicitation_setting import LexSlotValueElicitationSetting
from .lex_sub_slot_setting import LexSubSlotSetting


class LexCreateSlotResponse(BaseModel):
    slotId: StrictStr | None = None
    slotName: StrictStr | None = None
    description: StrictStr | None = None
    slotTypeId: StrictStr | None = None
    valueElicitationSetting: LexSlotValueElicitationSetting | None = None
    obfuscationSetting: LexObfuscationSetting | None = None
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    intentId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    multipleValuesSetting: LexMultipleValuesSetting | None = None
    subSlotSetting: LexSubSlotSetting | None = None
    ResponseMetadata: dict[str, Any] | None = None
