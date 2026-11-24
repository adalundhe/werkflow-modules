from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_connector_configuration import ConfigServiceConnectorConfiguration


class ConfigServiceConnector(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    connectorConfiguration: ConfigServiceConnectorConfiguration | None = None
    createdTime: datetime.datetime | StrictStr | None = None
