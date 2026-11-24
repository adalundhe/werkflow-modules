from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTopicIdentifierDeclaration(BaseModel):
    Identifier: StrictStr | None = None
    TopicArn: StrictStr | None = None
