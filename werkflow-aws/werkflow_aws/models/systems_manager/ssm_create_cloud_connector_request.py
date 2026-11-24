from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_cloud_connector_configuration import SSMCloudConnectorConfiguration
from .ssm_tag import SSMTag


class SSMCreateCloudConnectorRequest(BaseModel):
    DisplayName: StrictStr
    RoleArn: StrictStr
    Configuration: SSMCloudConnectorConfiguration
    Description: StrictStr | None = None
    ConfigConnectorArn: StrictStr | None = None
    Tags: list[SSMTag] | None = None
