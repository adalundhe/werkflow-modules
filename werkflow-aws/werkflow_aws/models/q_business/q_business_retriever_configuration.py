from __future__ import annotations
from pydantic import BaseModel
from .q_business_kendra_index_configuration import QBusinessKendraIndexConfiguration
from .q_business_native_index_configuration import QBusinessNativeIndexConfiguration


class QBusinessRetrieverConfiguration(BaseModel):
    nativeIndexConfiguration: QBusinessNativeIndexConfiguration | None = None
    kendraIndexConfiguration: QBusinessKendraIndexConfiguration | None = None
