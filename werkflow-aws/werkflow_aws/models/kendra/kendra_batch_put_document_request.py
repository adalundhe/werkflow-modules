from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_custom_document_enrichment_configuration import KendraCustomDocumentEnrichmentConfiguration
from .kendra_document import KendraDocument


class KendraBatchPutDocumentRequest(BaseModel):
    IndexId: StrictStr
    Documents: list[KendraDocument]
    RoleArn: StrictStr | None = None
    CustomDocumentEnrichmentConfiguration: KendraCustomDocumentEnrichmentConfiguration | None = None
