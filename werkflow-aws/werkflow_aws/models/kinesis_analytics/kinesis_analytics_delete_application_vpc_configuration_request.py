from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsDeleteApplicationVpcConfigurationRequest(BaseModel):
    ApplicationName: StrictStr
    VpcConfigurationId: StrictStr
    CurrentApplicationVersionId: StrictInt | None = None
    ConditionalToken: StrictStr | None = None
