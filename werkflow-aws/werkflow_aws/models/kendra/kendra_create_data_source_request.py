from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kendra_custom_document_enrichment_configuration import KendraCustomDocumentEnrichmentConfiguration
from .kendra_data_source_configuration import KendraDataSourceConfiguration
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration
from .kendra_tag import KendraTag


class KendraCreateDataSourceRequest(BaseModel):
    Name: StrictStr
    IndexId: StrictStr
    Type: Literal['S3', 'SHAREPOINT', 'DATABASE', 'SALESFORCE', 'ONEDRIVE', 'SERVICENOW', 'CUSTOM', 'CONFLUENCE', 'GOOGLEDRIVE', 'WEBCRAWLER', 'WORKDOCS', 'FSX', 'SLACK', 'BOX', 'QUIP', 'JIRA', 'GITHUB', 'ALFRESCO', 'TEMPLATE']
    Configuration: KendraDataSourceConfiguration | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    Description: StrictStr | None = None
    Schedule: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Tags: list[KendraTag] | None = None
    ClientToken: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    CustomDocumentEnrichmentConfiguration: KendraCustomDocumentEnrichmentConfiguration | None = None
