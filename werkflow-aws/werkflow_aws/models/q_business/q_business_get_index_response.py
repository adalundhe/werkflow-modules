from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_document_attribute_configuration import QBusinessDocumentAttributeConfiguration
from .q_business_error_detail import QBusinessErrorDetail
from .q_business_index_capacity_configuration import QBusinessIndexCapacityConfiguration
from .q_business_index_statistics import QBusinessIndexStatistics


class QBusinessGetIndexResponse(BaseModel):
    applicationId: StrictStr | None = None
    indexId: StrictStr | None = None
    displayName: StrictStr | None = None
    indexArn: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    capacityConfiguration: QBusinessIndexCapacityConfiguration | None = None
    documentAttributeConfigurations: list[QBusinessDocumentAttributeConfiguration] | None = None
    error: QBusinessErrorDetail | None = None
    indexStatistics: QBusinessIndexStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
