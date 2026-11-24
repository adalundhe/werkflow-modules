from __future__ import annotations
from pydantic import BaseModel
from .glue_connector_property import GlueConnectorProperty


class GlueBasicAuthenticationProperties(BaseModel):
    Username: GlueConnectorProperty | None = None
    Password: GlueConnectorProperty | None = None
