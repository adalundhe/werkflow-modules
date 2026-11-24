from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .wa_fv2_field_to_match import WAFv2FieldToMatch
from .wa_fv2_pre_parse_text_transformation import WAFv2PreParseTextTransformation
from .wa_fv2_text_transformation import WAFv2TextTransformation


class WAFv2ByteMatchStatement(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    SearchString: StrictBytes | Any | None = None
    FieldToMatch: WAFv2FieldToMatch | None = None
    TextTransformations: list[WAFv2TextTransformation] | None = None
    PreParseTextTransformations: list[WAFv2PreParseTextTransformation] | None = None
    PositionalConstraint: StrictStr | None = None
