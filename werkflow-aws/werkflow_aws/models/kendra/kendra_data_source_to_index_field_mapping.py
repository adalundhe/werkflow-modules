from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDataSourceToIndexFieldMapping(BaseModel):
    DataSourceFieldName: StrictStr | None = None
    DateFieldFormat: StrictStr | None = None
    IndexFieldName: StrictStr | None = None
