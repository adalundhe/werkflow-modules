from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .glue_connector_property import GlueConnectorProperty


class GlueJWTBearerProperties(BaseModel):
    TokenUrl: GlueConnectorProperty | None = None
    RequestMethod: Literal['GET', 'POST'] | None = None
    ContentType: Literal['APPLICATION_JSON', 'URL_ENCODED'] | None = None
    JwtToken: GlueConnectorProperty | None = None
    TokenUrlParameters: list[GlueConnectorProperty] | None = None
