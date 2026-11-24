from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_custom_response import WAFv2CustomResponse


class WAFv2BlockAction(BaseModel):
    CustomResponse: WAFv2CustomResponse | None = None
