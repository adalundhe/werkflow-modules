from __future__ import annotations
from pydantic import BaseModel
from .glue_connector_property import GlueConnectorProperty


class GlueConnectionPropertiesConfiguration(BaseModel):
    Url: GlueConnectorProperty | None = None
    AdditionalRequestParameters: list[GlueConnectorProperty] | None = None
