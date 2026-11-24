from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_application_attribute import WAFv2ApplicationAttribute


class WAFv2ApplicationConfig(BaseModel):
    Attributes: list[WAFv2ApplicationAttribute] | None = None
