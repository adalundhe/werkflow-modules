from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_orderable_cluster_option import RedshiftOrderableClusterOption


class RedshiftDescribeOrderableClusterOptionsResponse(BaseModel):
    OrderableClusterOptions: list[RedshiftOrderableClusterOption] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
