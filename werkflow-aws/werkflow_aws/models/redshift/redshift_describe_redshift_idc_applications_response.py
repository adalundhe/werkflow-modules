from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_idc_application import RedshiftIdcApplication


class RedshiftDescribeRedshiftIdcApplicationsResponse(BaseModel):
    RedshiftIdcApplications: list[RedshiftIdcApplication] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
