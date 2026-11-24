from __future__ import annotations
from pydantic import BaseModel
from .open_search_option_status import OpenSearchOptionStatus
from .open_search_snapshot_options import OpenSearchSnapshotOptions


class OpenSearchSnapshotOptionsStatus(BaseModel):
    Options: OpenSearchSnapshotOptions | None = None
    Status: OpenSearchOptionStatus | None = None
