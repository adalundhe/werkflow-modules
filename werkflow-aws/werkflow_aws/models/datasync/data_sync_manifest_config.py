from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_source_manifest_config import DataSyncSourceManifestConfig


class DataSyncManifestConfig(BaseModel):
    Action: StrictStr | None = None
    Format: StrictStr | None = None
    Source: DataSyncSourceManifestConfig | None = None
