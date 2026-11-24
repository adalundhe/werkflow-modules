from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_configuration_revision_model import MSKConfigurationRevisionModel


class MSKCreateConfigurationResponse(BaseModel):
    Arn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LatestRevision: MSKConfigurationRevisionModel | None = None
    Name: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
