from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .q_business_document_attribute_boosting_configuration import QBusinessDocumentAttributeBoostingConfiguration


class QBusinessNativeIndexConfiguration(BaseModel):
    indexId: StrictStr | None = None
    version: StrictInt | None = None
    boostingOverride: dict[StrictStr, QBusinessDocumentAttributeBoostingConfiguration] | None = None
