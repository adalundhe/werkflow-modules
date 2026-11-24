from __future__ import annotations
from typing import TypeAlias
from .mandatory_field_value import MandatoryFieldValue
from .mandatory_field_value_for_adf import MandatoryFieldValueForADF

MandatoryFieldValueUnion: TypeAlias = MandatoryFieldValue | MandatoryFieldValueForADF
