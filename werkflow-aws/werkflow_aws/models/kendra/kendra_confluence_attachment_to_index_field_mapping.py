from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraConfluenceAttachmentToIndexFieldMapping(BaseModel):
    DataSourceFieldName: StrictStr | None = None
    DateFieldFormat: StrictStr | None = None
    IndexFieldName: StrictStr | None = None
