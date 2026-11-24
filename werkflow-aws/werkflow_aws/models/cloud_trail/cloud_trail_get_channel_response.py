from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_destination import CloudTrailDestination
from .cloud_trail_ingestion_status import CloudTrailIngestionStatus
from .cloud_trail_source_config import CloudTrailSourceConfig


class CloudTrailGetChannelResponse(BaseModel):
    ChannelArn: StrictStr | None = None
    Name: StrictStr | None = None
    Source: StrictStr | None = None
    SourceConfig: CloudTrailSourceConfig | None = None
    Destinations: list[CloudTrailDestination] | None = None
    IngestionStatus: CloudTrailIngestionStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
