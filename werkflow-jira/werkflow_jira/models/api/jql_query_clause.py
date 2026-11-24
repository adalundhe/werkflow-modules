from __future__ import annotations
from typing import TypeAlias
from .compound_clause import CompoundClause
from .field_changed_clause import FieldChangedClause
from .field_value_clause import FieldValueClause
from .field_was_clause import FieldWasClause

JqlQueryClause: TypeAlias = CompoundClause | FieldValueClause | FieldWasClause | FieldChangedClause
