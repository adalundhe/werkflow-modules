from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightS3KnowledgeBaseParameters(BaseModel):
    RoleArn: StrictStr | None = None
    BucketUrl: StrictStr | None = None
    MetadataFilesLocation: StrictStr | None = None
