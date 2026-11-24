from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_describe_db_log_files_details import RDSDescribeDBLogFilesDetails


class RDSDescribeDBLogFilesResponse(BaseModel):
    DescribeDBLogFiles: list[RDSDescribeDBLogFilesDetails] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
