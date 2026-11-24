from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_reference_data_source_description import KinesisAnalyticsReferenceDataSourceDescription


class KinesisAnalyticsAddApplicationReferenceDataSourceResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    ReferenceDataSourceDescriptions: list[KinesisAnalyticsReferenceDataSourceDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
