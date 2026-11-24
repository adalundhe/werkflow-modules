from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_default_cluster_parameters import RedshiftDefaultClusterParameters


class RedshiftDescribeDefaultClusterParametersResponse(BaseModel):
    DefaultClusterParameters: RedshiftDefaultClusterParameters | None = None
    ResponseMetadata: dict[str, Any] | None = None
