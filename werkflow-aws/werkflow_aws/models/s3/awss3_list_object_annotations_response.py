from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_annotation_entry import AWSS3AnnotationEntry


class AWSS3ListObjectAnnotationsResponse(BaseModel):
    Annotations: list[AWSS3AnnotationEntry] | None = None
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
    ObjectVersionId: StrictStr | None = None
    AnnotationPrefix: StrictStr | None = None
    MaxAnnotationResults: StrictInt | None = None
    AnnotationCount: StrictInt | None = None
    ContinuationToken: StrictStr | None = None
    NextContinuationToken: StrictStr | None = None
    RequestCharged: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
