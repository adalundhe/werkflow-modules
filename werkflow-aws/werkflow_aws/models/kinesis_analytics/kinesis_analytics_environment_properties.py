from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_property_group import KinesisAnalyticsPropertyGroup


class KinesisAnalyticsEnvironmentProperties(BaseModel):
    PropertyGroups: list[KinesisAnalyticsPropertyGroup]
