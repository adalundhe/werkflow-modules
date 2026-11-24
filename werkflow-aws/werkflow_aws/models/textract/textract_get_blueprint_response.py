from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class TextractGetBlueprintResponse(BaseModel):
    BlueprintArn: StrictStr | None = None
    BlueprintName: StrictStr | None = None
    BlueprintVersion: StrictStr | None = None
    Schema: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    KmsEncryptionContext: dict[StrictStr, StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
