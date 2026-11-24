from __future__ import annotations
from pydantic import BaseModel
from .glue_connector_property import GlueConnectorProperty


class GlueCustomAuthenticationProperties(BaseModel):
    AuthenticationParameters: list[GlueConnectorProperty]
