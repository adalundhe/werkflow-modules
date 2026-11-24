from __future__ import annotations
from pydantic import BaseModel
from .ses_cloud_watch_dimension_configuration import SESCloudWatchDimensionConfiguration


class SESCloudWatchDestination(BaseModel):
    DimensionConfigurations: list[SESCloudWatchDimensionConfiguration] | None = None
