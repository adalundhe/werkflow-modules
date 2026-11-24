from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_data_source_configuration import QBusinessDataSourceConfiguration
from .q_business_data_source_vpc_configuration import QBusinessDataSourceVpcConfiguration
from .q_business_document_enrichment_configuration import QBusinessDocumentEnrichmentConfiguration
from .q_business_media_extraction_configuration import QBusinessMediaExtractionConfiguration


class QBusinessUpdateDataSourceRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    dataSourceId: StrictStr
    displayName: StrictStr | None = None
    configuration: QBusinessDataSourceConfiguration | None = None
    vpcConfiguration: QBusinessDataSourceVpcConfiguration | None = None
    description: StrictStr | None = None
    syncSchedule: StrictStr | None = None
    roleArn: StrictStr | None = None
    documentEnrichmentConfiguration: QBusinessDocumentEnrichmentConfiguration | None = None
    mediaExtractionConfiguration: QBusinessMediaExtractionConfiguration | None = None
