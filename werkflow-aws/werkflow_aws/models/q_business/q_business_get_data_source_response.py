from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_data_source_configuration import QBusinessDataSourceConfiguration
from .q_business_data_source_vpc_configuration import QBusinessDataSourceVpcConfiguration
from .q_business_document_enrichment_configuration import QBusinessDocumentEnrichmentConfiguration
from .q_business_error_detail import QBusinessErrorDetail
from .q_business_media_extraction_configuration import QBusinessMediaExtractionConfiguration


class QBusinessGetDataSourceResponse(BaseModel):
    applicationId: StrictStr | None = None
    indexId: StrictStr | None = None
    dataSourceId: StrictStr | None = None
    dataSourceArn: StrictStr | None = None
    displayName: StrictStr | None = None
    type: StrictStr | None = None
    configuration: QBusinessDataSourceConfiguration | None = None
    vpcConfiguration: QBusinessDataSourceVpcConfiguration | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    syncSchedule: StrictStr | None = None
    roleArn: StrictStr | None = None
    error: QBusinessErrorDetail | None = None
    documentEnrichmentConfiguration: QBusinessDocumentEnrichmentConfiguration | None = None
    mediaExtractionConfiguration: QBusinessMediaExtractionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
