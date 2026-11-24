from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_cloud_connector_configuration import SSMCloudConnectorConfiguration


class SSMUpdateCloudConnectorRequest(BaseModel):
    CloudConnectorId: StrictStr
    DisplayName: StrictStr | None = None
    Configuration: SSMCloudConnectorConfiguration | None = None
    Description: StrictStr | None = None
