from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_aqua_configuration import RedshiftAquaConfiguration


class RedshiftModifyAquaConfigurationResponse(BaseModel):
    AquaConfiguration: RedshiftAquaConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
