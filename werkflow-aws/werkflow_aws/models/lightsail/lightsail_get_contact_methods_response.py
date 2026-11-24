from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_contact_method import LightsailContactMethod


class LightsailGetContactMethodsResponse(BaseModel):
    contactMethods: list[LightsailContactMethod] | None = None
    ResponseMetadata: dict[str, Any] | None = None
