from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_test_set_generation_data_source import LexTestSetGenerationDataSource
from .lex_test_set_storage_location import LexTestSetStorageLocation


class LexStartTestSetGenerationRequest(BaseModel):
    testSetName: StrictStr
    storageLocation: LexTestSetStorageLocation
    generationDataSource: LexTestSetGenerationDataSource
    roleArn: StrictStr
    description: StrictStr | None = None
    testSetTags: dict[StrictStr, StrictStr] | None = None
