from __future__ import annotations
from pydantic import BaseModel
from .q_business_hook_configuration import QBusinessHookConfiguration
from .q_business_inline_document_enrichment_configuration import QBusinessInlineDocumentEnrichmentConfiguration


class QBusinessDocumentEnrichmentConfiguration(BaseModel):
    inlineConfigurations: list[QBusinessInlineDocumentEnrichmentConfiguration] | None = None
    preExtractionHookConfiguration: QBusinessHookConfiguration | None = None
    postExtractionHookConfiguration: QBusinessHookConfiguration | None = None
