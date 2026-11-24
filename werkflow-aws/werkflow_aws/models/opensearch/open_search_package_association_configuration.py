from __future__ import annotations
from pydantic import BaseModel
from .open_search_key_store_access_option import OpenSearchKeyStoreAccessOption


class OpenSearchPackageAssociationConfiguration(BaseModel):
    KeyStoreAccessOption: OpenSearchKeyStoreAccessOption | None = None
