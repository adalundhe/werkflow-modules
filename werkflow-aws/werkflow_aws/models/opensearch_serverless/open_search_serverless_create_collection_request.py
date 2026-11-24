from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_serverless_encryption_config import OpenSearchServerlessEncryptionConfig
from .open_search_serverless_tag import OpenSearchServerlessTag
from .open_search_serverless_vector_options import OpenSearchServerlessVectorOptions


class OpenSearchServerlessCreateCollectionRequest(BaseModel):
    name: StrictStr
    type: Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH'] | None = None
    description: StrictStr | None = None
    tags: list[OpenSearchServerlessTag] | None = None
    standbyReplicas: Literal['ENABLED', 'DISABLED'] | None = None
    vectorOptions: OpenSearchServerlessVectorOptions | None = None
    collectionGroupName: StrictStr | None = None
    encryptionConfig: OpenSearchServerlessEncryptionConfig | None = None
    deletionProtection: Literal['ENABLED', 'DISABLED'] | None = None
    clientToken: StrictStr | None = None
