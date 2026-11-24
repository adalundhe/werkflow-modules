from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_vpc_configuration_description import KinesisAnalyticsVpcConfigurationDescription


class KinesisAnalyticsAddApplicationVpcConfigurationResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    VpcConfigurationDescription: KinesisAnalyticsVpcConfigurationDescription | None = None
    OperationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
