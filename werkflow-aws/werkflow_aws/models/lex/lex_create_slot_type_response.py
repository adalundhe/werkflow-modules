from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_composite_slot_type_setting import LexCompositeSlotTypeSetting
from .lex_external_source_setting import LexExternalSourceSetting
from .lex_slot_type_value import LexSlotTypeValue
from .lex_slot_value_selection_setting import LexSlotValueSelectionSetting


class LexCreateSlotTypeResponse(BaseModel):
    slotTypeId: StrictStr | None = None
    slotTypeName: StrictStr | None = None
    description: StrictStr | None = None
    slotTypeValues: list[LexSlotTypeValue] | None = None
    valueSelectionSetting: LexSlotValueSelectionSetting | None = None
    parentSlotTypeSignature: StrictStr | None = None
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    externalSourceSetting: LexExternalSourceSetting | None = None
    compositeSlotTypeSetting: LexCompositeSlotTypeSetting | None = None
    ResponseMetadata: dict[str, Any] | None = None
