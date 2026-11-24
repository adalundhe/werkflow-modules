from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_qev2_idc_application import RedshiftQev2IdcApplication


class RedshiftDescribeQev2IdcApplicationsResponse(BaseModel):
    Qev2IdcApplications: list[RedshiftQev2IdcApplication] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
