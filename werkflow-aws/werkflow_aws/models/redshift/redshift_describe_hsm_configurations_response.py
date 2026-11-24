from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_hsm_configuration import RedshiftHsmConfiguration


class RedshiftDescribeHsmConfigurationsResponse(BaseModel):
    Marker: StrictStr | None = None
    HsmConfigurations: list[RedshiftHsmConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
