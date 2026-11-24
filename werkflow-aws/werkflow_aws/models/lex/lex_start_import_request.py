from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lex_import_resource_specification import LexImportResourceSpecification


class LexStartImportRequest(BaseModel):
    importId: StrictStr
    resourceSpecification: LexImportResourceSpecification
    mergeStrategy: Literal['Overwrite', 'FailOnConflict', 'Append']
    filePassword: StrictStr | None = None
