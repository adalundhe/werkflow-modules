from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_templates_response import PinpointTemplatesResponse


class PinpointListTemplatesResponse(BaseModel):
    TemplatesResponse: PinpointTemplatesResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
