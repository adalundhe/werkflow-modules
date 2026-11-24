from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_node_configuration_option import RedshiftNodeConfigurationOption


class RedshiftDescribeNodeConfigurationOptionsResponse(BaseModel):
    NodeConfigurationOptionList: list[RedshiftNodeConfigurationOption] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
