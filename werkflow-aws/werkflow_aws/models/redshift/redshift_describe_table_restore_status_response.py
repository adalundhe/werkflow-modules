from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_table_restore_status import RedshiftTableRestoreStatus


class RedshiftDescribeTableRestoreStatusResponse(BaseModel):
    TableRestoreStatusDetails: list[RedshiftTableRestoreStatus] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
