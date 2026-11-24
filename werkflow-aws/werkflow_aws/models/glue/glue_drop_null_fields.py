from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_null_check_box_list import GlueNullCheckBoxList
from .glue_null_value_field import GlueNullValueField


class GlueDropNullFields(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    NullCheckBoxList: GlueNullCheckBoxList | None = None
    NullTextList: list[GlueNullValueField] | None = None
