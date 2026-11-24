from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendDatasetAugmentedManifestsListItem(BaseModel):
    AttributeNames: list[StrictStr]
    S3Uri: StrictStr
    AnnotationDataS3Uri: StrictStr | None = None
    SourceDocumentsS3Uri: StrictStr | None = None
    DocumentType: Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT'] | None = None
