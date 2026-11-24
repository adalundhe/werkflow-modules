from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_custom_document_enrichment_configuration import KendraCustomDocumentEnrichmentConfiguration
from .kendra_data_source_configuration import KendraDataSourceConfiguration
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration


class KendraDescribeDataSourceResponse(BaseModel):
    Id: StrictStr | None = None
    IndexId: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Configuration: KendraDataSourceConfiguration | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    Schedule: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    CustomDocumentEnrichmentConfiguration: KendraCustomDocumentEnrichmentConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
