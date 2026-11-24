from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .mq_configuration_revision import MQConfigurationRevision
from .mq_sanitization_warning import MQSanitizationWarning


class MQUpdateConfigurationResponse(BaseModel):
    Arn: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    Id: StrictStr | None = None
    LatestRevision: MQConfigurationRevision | None = None
    Name: StrictStr | None = None
    Warnings: list[MQSanitizationWarning] | None = None
    ResponseMetadata: dict[str, Any] | None = None
