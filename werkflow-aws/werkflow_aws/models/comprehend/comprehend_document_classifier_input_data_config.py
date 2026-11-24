from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_augmented_manifests_list_item import ComprehendAugmentedManifestsListItem
from .comprehend_document_classifier_documents import ComprehendDocumentClassifierDocuments
from .comprehend_document_reader_config import ComprehendDocumentReaderConfig


class ComprehendDocumentClassifierInputDataConfig(BaseModel):
    DataFormat: StrictStr | None = None
    S3Uri: StrictStr | None = None
    TestS3Uri: StrictStr | None = None
    LabelDelimiter: StrictStr | None = None
    AugmentedManifests: list[ComprehendAugmentedManifestsListItem] | None = None
    DocumentType: StrictStr | None = None
    Documents: ComprehendDocumentClassifierDocuments | None = None
    DocumentReaderConfig: ComprehendDocumentReaderConfig | None = None
