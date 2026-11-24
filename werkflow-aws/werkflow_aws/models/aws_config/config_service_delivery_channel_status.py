from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_config_export_delivery_info import ConfigServiceConfigExportDeliveryInfo
from .config_service_config_stream_delivery_info import ConfigServiceConfigStreamDeliveryInfo


class ConfigServiceDeliveryChannelStatus(BaseModel):
    name: StrictStr | None = None
    configSnapshotDeliveryInfo: ConfigServiceConfigExportDeliveryInfo | None = None
    configHistoryDeliveryInfo: ConfigServiceConfigExportDeliveryInfo | None = None
    configStreamDeliveryInfo: ConfigServiceConfigStreamDeliveryInfo | None = None
