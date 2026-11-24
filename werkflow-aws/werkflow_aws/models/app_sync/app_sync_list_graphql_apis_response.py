from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_graphql_api import AppSyncGraphqlApi


class AppSyncListGraphqlApisResponse(BaseModel):
    graphqlApis: list[AppSyncGraphqlApi] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
