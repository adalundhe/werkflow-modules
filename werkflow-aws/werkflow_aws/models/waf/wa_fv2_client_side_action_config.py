from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_client_side_action import WAFv2ClientSideAction


class WAFv2ClientSideActionConfig(BaseModel):
    Challenge: WAFv2ClientSideAction | None = None
