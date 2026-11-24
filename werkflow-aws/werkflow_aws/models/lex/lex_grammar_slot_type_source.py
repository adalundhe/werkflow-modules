from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexGrammarSlotTypeSource(BaseModel):
    s3BucketName: StrictStr | None = None
    s3ObjectKey: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
