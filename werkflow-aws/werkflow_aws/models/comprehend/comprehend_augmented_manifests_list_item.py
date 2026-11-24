from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendAugmentedManifestsListItem(BaseModel):
    S3Uri: StrictStr | None = None
    Split: StrictStr | None = None
    AttributeNames: list[StrictStr] | None = None
    AnnotationDataS3Uri: StrictStr | None = None
    SourceDocumentsS3Uri: StrictStr | None = None
    DocumentType: StrictStr | None = None
