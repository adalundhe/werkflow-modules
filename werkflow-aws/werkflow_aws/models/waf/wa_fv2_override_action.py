from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .wa_fv2_count_action import WAFv2CountAction
from .wa_fv2_none_action import WAFv2NoneAction


class WAFv2OverrideAction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    Count: WAFv2CountAction | None = None
    None_: WAFv2NoneAction | None = Field(default=None, alias='None')
