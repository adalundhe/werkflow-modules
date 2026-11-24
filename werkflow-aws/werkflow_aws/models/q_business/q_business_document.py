from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_access_configuration import QBusinessAccessConfiguration
from .q_business_document_attribute import QBusinessDocumentAttribute
from .q_business_document_content import QBusinessDocumentContent
from .q_business_document_enrichment_configuration import QBusinessDocumentEnrichmentConfiguration
from .q_business_media_extraction_configuration import QBusinessMediaExtractionConfiguration


class QBusinessDocument(BaseModel):
    id: StrictStr
    attributes: list[QBusinessDocumentAttribute] | None = None
    content: QBusinessDocumentContent | None = None
    contentType: Literal['PDF', 'HTML', 'MS_WORD', 'PLAIN_TEXT', 'PPT', 'RTF', 'XML', 'XSLT', 'MS_EXCEL', 'CSV', 'JSON', 'MD'] | None = None
    title: StrictStr | None = None
    accessConfiguration: QBusinessAccessConfiguration | None = None
    documentEnrichmentConfiguration: QBusinessDocumentEnrichmentConfiguration | None = None
    mediaExtractionConfiguration: QBusinessMediaExtractionConfiguration | None = None
