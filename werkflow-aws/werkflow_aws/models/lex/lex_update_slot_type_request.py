from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_composite_slot_type_setting import LexCompositeSlotTypeSetting
from .lex_external_source_setting import LexExternalSourceSetting
from .lex_slot_type_value import LexSlotTypeValue
from .lex_slot_value_selection_setting import LexSlotValueSelectionSetting


class LexUpdateSlotTypeRequest(BaseModel):
    slotTypeId: StrictStr
    slotTypeName: StrictStr
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    description: StrictStr | None = None
    slotTypeValues: list[LexSlotTypeValue] | None = None
    valueSelectionSetting: LexSlotValueSelectionSetting | None = None
    parentSlotTypeSignature: StrictStr | None = None
    externalSourceSetting: LexExternalSourceSetting | None = None
    compositeSlotTypeSetting: LexCompositeSlotTypeSetting | None = None
