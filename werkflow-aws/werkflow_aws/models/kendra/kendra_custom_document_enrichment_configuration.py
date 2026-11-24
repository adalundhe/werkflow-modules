from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_hook_configuration import KendraHookConfiguration
from .kendra_inline_custom_document_enrichment_configuration import KendraInlineCustomDocumentEnrichmentConfiguration


class KendraCustomDocumentEnrichmentConfiguration(BaseModel):
    InlineConfigurations: list[KendraInlineCustomDocumentEnrichmentConfiguration] | None = None
    PreExtractionHookConfiguration: KendraHookConfiguration | None = None
    PostExtractionHookConfiguration: KendraHookConfiguration | None = None
    RoleArn: StrictStr | None = None
