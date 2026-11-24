from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_property_group import KinesisAnalyticsPropertyGroup


class KinesisAnalyticsEnvironmentPropertyUpdates(BaseModel):
    PropertyGroups: list[KinesisAnalyticsPropertyGroup]
