from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_filter import FSxFilter


class FSxDescribeBackupsRequest(BaseModel):
    BackupIds: list[StrictStr] | None = None
    Filters: list[FSxFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
