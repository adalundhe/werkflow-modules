from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_allow_action import WAFv2AllowAction
from .wa_fv2_block_action import WAFv2BlockAction


class WAFv2DefaultAction(BaseModel):
    Block: WAFv2BlockAction | None = None
    Allow: WAFv2AllowAction | None = None
