from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_graphql_api import AppSyncGraphqlApi


class AppSyncGetGraphqlApiResponse(BaseModel):
    graphqlApi: AppSyncGraphqlApi | None = None
    ResponseMetadata: dict[str, Any] | None = None
