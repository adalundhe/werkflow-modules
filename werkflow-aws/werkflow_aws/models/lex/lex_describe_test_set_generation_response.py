from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_set_generation_data_source import LexTestSetGenerationDataSource
from .lex_test_set_storage_location import LexTestSetStorageLocation


class LexDescribeTestSetGenerationResponse(BaseModel):
    testSetGenerationId: StrictStr | None = None
    testSetGenerationStatus: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    testSetId: StrictStr | None = None
    testSetName: StrictStr | None = None
    description: StrictStr | None = None
    storageLocation: LexTestSetStorageLocation | None = None
    generationDataSource: LexTestSetGenerationDataSource | None = None
    roleArn: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
