from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncListGraphqlApisRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    apiType: Literal['GRAPHQL', 'MERGED'] | None = None
    owner: Literal['CURRENT_ACCOUNT', 'OTHER_ACCOUNTS'] | None = None
