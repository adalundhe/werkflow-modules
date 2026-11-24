from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_security_configuration import GlueSecurityConfiguration


class GlueGetSecurityConfigurationResponse(BaseModel):
    SecurityConfiguration: GlueSecurityConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
