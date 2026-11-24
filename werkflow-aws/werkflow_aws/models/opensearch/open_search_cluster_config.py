from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .open_search_cold_storage_options import OpenSearchColdStorageOptions
from .open_search_node_option import OpenSearchNodeOption
from .open_search_zone_awareness_config import OpenSearchZoneAwarenessConfig


class OpenSearchClusterConfig(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    DedicatedMasterEnabled: StrictBool | None = None
    ZoneAwarenessEnabled: StrictBool | None = None
    ZoneAwarenessConfig: OpenSearchZoneAwarenessConfig | None = None
    DedicatedMasterType: StrictStr | None = None
    DedicatedMasterCount: StrictInt | None = None
    WarmEnabled: StrictBool | None = None
    WarmType: StrictStr | None = None
    WarmCount: StrictInt | None = None
    ColdStorageOptions: OpenSearchColdStorageOptions | None = None
    MultiAZWithStandbyEnabled: StrictBool | None = None
    NodeOptions: list[OpenSearchNodeOption] | None = None
