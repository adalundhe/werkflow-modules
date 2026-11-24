from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class OpenSearchListDomainNamesRequest(BaseModel):
    EngineType: Literal['OpenSearch', 'Elasticsearch'] | None = None
