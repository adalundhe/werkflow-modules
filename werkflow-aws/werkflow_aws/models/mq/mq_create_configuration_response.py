from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .mq_configuration_revision import MQConfigurationRevision


class MQCreateConfigurationResponse(BaseModel):
    Arn: StrictStr | None = None
    AuthenticationStrategy: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    Id: StrictStr | None = None
    LatestRevision: MQConfigurationRevision | None = None
    Name: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
