from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_reserved_node_configuration_option import RedshiftReservedNodeConfigurationOption


class RedshiftGetReservedNodeExchangeConfigurationOptionsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReservedNodeConfigurationOptionList: list[RedshiftReservedNodeConfigurationOption] | None = None
    ResponseMetadata: dict[str, Any] | None = None
