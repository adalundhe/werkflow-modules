from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_custom_document_enrichment_configuration import KendraCustomDocumentEnrichmentConfiguration
from .kendra_data_source_configuration import KendraDataSourceConfiguration
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration


class KendraUpdateDataSourceRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    Name: StrictStr | None = None
    Configuration: KendraDataSourceConfiguration | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    Description: StrictStr | None = None
    Schedule: StrictStr | None = None
    RoleArn: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    CustomDocumentEnrichmentConfiguration: KendraCustomDocumentEnrichmentConfiguration | None = None
