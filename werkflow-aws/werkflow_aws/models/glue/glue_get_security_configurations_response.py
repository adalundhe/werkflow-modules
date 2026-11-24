from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_security_configuration import GlueSecurityConfiguration


class GlueGetSecurityConfigurationsResponse(BaseModel):
    SecurityConfigurations: list[GlueSecurityConfiguration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
