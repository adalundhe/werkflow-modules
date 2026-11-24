from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_maintenance_configuration_description import KinesisAnalyticsApplicationMaintenanceConfigurationDescription


class KinesisAnalyticsUpdateApplicationMaintenanceConfigurationResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationMaintenanceConfigurationDescription: KinesisAnalyticsApplicationMaintenanceConfigurationDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
