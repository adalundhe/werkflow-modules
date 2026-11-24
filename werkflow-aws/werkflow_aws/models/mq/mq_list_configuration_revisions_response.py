from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .mq_configuration_revision import MQConfigurationRevision


class MQListConfigurationRevisionsResponse(BaseModel):
    ConfigurationId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Revisions: list[MQConfigurationRevision] | None = None
    ResponseMetadata: dict[str, Any] | None = None
