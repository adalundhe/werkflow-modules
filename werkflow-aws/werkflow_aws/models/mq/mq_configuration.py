from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .mq_configuration_revision import MQConfigurationRevision


class MQConfiguration(BaseModel):
    Arn: StrictStr | None = None
    AuthenticationStrategy: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    EngineType: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Id: StrictStr | None = None
    LatestRevision: MQConfigurationRevision | None = None
    Name: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
