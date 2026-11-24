from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_parameter import DocumentDBParameter


class DocumentDBEngineDefaults(BaseModel):
    DBParameterGroupFamily: StrictStr | None = None
    Marker: StrictStr | None = None
    Parameters: list[DocumentDBParameter] | None = None
