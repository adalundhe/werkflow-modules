from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_test_set_import_input_location import LexTestSetImportInputLocation
from .lex_test_set_storage_location import LexTestSetStorageLocation


class LexTestSetImportResourceSpecification(BaseModel):
    testSetName: StrictStr | None = None
    description: StrictStr | None = None
    roleArn: StrictStr | None = None
    storageLocation: LexTestSetStorageLocation | None = None
    importInputLocation: LexTestSetImportInputLocation | None = None
    modality: StrictStr | None = None
    testSetTags: dict[StrictStr, StrictStr] | None = None
