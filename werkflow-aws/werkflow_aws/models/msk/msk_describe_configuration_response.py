from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .msk_configuration_revision import MSKConfigurationRevision


class MSKDescribeConfigurationResponse(BaseModel):
    Arn: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    Description: StrictStr | None = None
    KafkaVersions: list[StrictStr] | None = None
    LatestRevision: MSKConfigurationRevision | None = None
    Name: StrictStr | None = None
    State: StrictStr | None = None
