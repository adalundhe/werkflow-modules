from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .textract_geometry import TextractGeometry
from .textract_query import TextractQuery
from .textract_relationship import TextractRelationship


class TextractBlock(BaseModel):
    BlockType: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Text: StrictStr | None = None
    TextType: StrictStr | None = None
    RowIndex: StrictInt | None = None
    ColumnIndex: StrictInt | None = None
    RowSpan: StrictInt | None = None
    ColumnSpan: StrictInt | None = None
    Geometry: TextractGeometry | None = None
    Id: StrictStr | None = None
    Relationships: list[TextractRelationship] | None = None
    EntityTypes: list[StrictStr] | None = None
    SelectionStatus: StrictStr | None = None
    Page: StrictInt | None = None
    Query: TextractQuery | None = None
