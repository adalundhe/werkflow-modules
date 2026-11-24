from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .glue_connector_property import GlueConnectorProperty


class GlueConnectorAuthorizationCodeProperties(BaseModel):
    AuthorizationCodeUrl: GlueConnectorProperty | None = None
    AuthorizationCode: GlueConnectorProperty | None = None
    RedirectUri: GlueConnectorProperty | None = None
    TokenUrl: GlueConnectorProperty | None = None
    RequestMethod: Literal['GET', 'POST'] | None = None
    ContentType: Literal['APPLICATION_JSON', 'URL_ENCODED'] | None = None
    ClientId: GlueConnectorProperty | None = None
    ClientSecret: GlueConnectorProperty | None = None
    Scope: GlueConnectorProperty | None = None
    Prompt: GlueConnectorProperty | None = None
    TokenUrlParameters: list[GlueConnectorProperty] | None = None
