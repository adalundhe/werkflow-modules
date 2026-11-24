from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_serverless_encryption_config import OpenSearchServerlessEncryptionConfig
from .open_search_serverless_vector_options import OpenSearchServerlessVectorOptions


class OpenSearchServerlessUpdateCollectionRequest(BaseModel):
    id: StrictStr
    description: StrictStr | None = None
    vectorOptions: OpenSearchServerlessVectorOptions | None = None
    deletionProtection: Literal['ENABLED', 'DISABLED'] | None = None
    encryptionConfig: OpenSearchServerlessEncryptionConfig | None = None
    clientToken: StrictStr | None = None
