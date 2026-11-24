from __future__ import annotations
from pydantic import BaseModel
from .association_context_object import AssociationContextObject
from .field_identifier_object import FieldIdentifierObject


class FieldAssociationsRequest(BaseModel):
    associationContexts: list[AssociationContextObject] | None = None
    fields: list[FieldIdentifierObject] | None = None
