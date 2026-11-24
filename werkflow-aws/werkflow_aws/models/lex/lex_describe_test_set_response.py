from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_test_set_storage_location import LexTestSetStorageLocation


class LexDescribeTestSetResponse(BaseModel):
    testSetId: StrictStr | None = None
    testSetName: StrictStr | None = None
    description: StrictStr | None = None
    modality: StrictStr | None = None
    status: StrictStr | None = None
    roleArn: StrictStr | None = None
    numTurns: StrictInt | None = None
    storageLocation: LexTestSetStorageLocation | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
