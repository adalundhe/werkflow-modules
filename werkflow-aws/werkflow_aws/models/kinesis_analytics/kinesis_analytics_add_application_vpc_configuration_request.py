from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_vpc_configuration import KinesisAnalyticsVpcConfiguration


class KinesisAnalyticsAddApplicationVpcConfigurationRequest(BaseModel):
    ApplicationName: StrictStr
    VpcConfiguration: KinesisAnalyticsVpcConfiguration
    CurrentApplicationVersionId: StrictInt | None = None
    ConditionalToken: StrictStr | None = None
