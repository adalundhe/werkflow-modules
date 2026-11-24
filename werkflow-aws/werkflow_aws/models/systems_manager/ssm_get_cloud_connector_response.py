from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_cloud_connector_configuration import SSMCloudConnectorConfiguration


class SSMGetCloudConnectorResponse(BaseModel):
    CloudConnectorArn: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Configuration: SSMCloudConnectorConfiguration | None = None
    ConfigConnectorArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
