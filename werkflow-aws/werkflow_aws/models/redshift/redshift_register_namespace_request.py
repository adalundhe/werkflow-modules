from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_namespace_identifier_union import RedshiftNamespaceIdentifierUnion


class RedshiftRegisterNamespaceRequest(BaseModel):
    NamespaceIdentifier: RedshiftNamespaceIdentifierUnion
    ConsumerIdentifiers: list[StrictStr]
