from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_advanced_recognition_setting import LexAdvancedRecognitionSetting
from .lex_slot_value_regex_filter import LexSlotValueRegexFilter


class LexSlotValueSelectionSetting(BaseModel):
    resolutionStrategy: StrictStr | None = None
    regexFilter: LexSlotValueRegexFilter | None = None
    advancedRecognitionSetting: LexAdvancedRecognitionSetting | None = None
