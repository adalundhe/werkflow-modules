from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_connection_properties_configuration import GlueConnectionPropertiesConfiguration
from .glue_connector_authentication_configuration import GlueConnectorAuthenticationConfiguration
from .glue_rest_configuration import GlueRestConfiguration


class GlueRegisterConnectionTypeRequest(BaseModel):
    ConnectionType: StrictStr
    IntegrationType: Literal['REST']
    ConnectionProperties: GlueConnectionPropertiesConfiguration
    ConnectorAuthenticationConfiguration: GlueConnectorAuthenticationConfiguration
    RestConfiguration: GlueRestConfiguration
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
