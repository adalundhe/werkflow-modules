from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .mandatory_field_value_union import MandatoryFieldValueUnion


class TargetMandatoryFields(BaseModel):
    fields: dict[StrictStr, MandatoryFieldValueUnion] | None = None
