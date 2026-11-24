from __future__ import annotations
from pydantic import BaseModel
from .open_search_automated_snapshot_pause_options import OpenSearchAutomatedSnapshotPauseOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchAutomatedSnapshotPauseOptionsStatus(BaseModel):
    Options: OpenSearchAutomatedSnapshotPauseOptions | None = None
    Status: OpenSearchOptionStatus | None = None
