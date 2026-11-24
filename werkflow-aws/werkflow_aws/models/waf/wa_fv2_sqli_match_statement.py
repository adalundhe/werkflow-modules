from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_field_to_match import WAFv2FieldToMatch
from .wa_fv2_pre_parse_text_transformation import WAFv2PreParseTextTransformation
from .wa_fv2_text_transformation import WAFv2TextTransformation


class WAFv2SqliMatchStatement(BaseModel):
    FieldToMatch: WAFv2FieldToMatch | None = None
    TextTransformations: list[WAFv2TextTransformation] | None = None
    PreParseTextTransformations: list[WAFv2PreParseTextTransformation] | None = None
    SensitivityLevel: StrictStr | None = None
