from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_hsm_configuration import RedshiftHsmConfiguration


class RedshiftCreateHsmConfigurationResponse(BaseModel):
    HsmConfiguration: RedshiftHsmConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
