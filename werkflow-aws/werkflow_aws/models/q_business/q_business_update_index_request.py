from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document_attribute_configuration import QBusinessDocumentAttributeConfiguration
from .q_business_index_capacity_configuration import QBusinessIndexCapacityConfiguration


class QBusinessUpdateIndexRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    capacityConfiguration: QBusinessIndexCapacityConfiguration | None = None
    documentAttributeConfigurations: list[QBusinessDocumentAttributeConfiguration] | None = None
