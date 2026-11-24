from __future__ import annotations
from pydantic import BaseModel
from .redshift_provisioned_identifier import RedshiftProvisionedIdentifier
from .redshift_serverless_identifier import RedshiftServerlessIdentifier


class RedshiftNamespaceIdentifierUnion(BaseModel):
    ServerlessIdentifier: RedshiftServerlessIdentifier | None = None
    ProvisionedIdentifier: RedshiftProvisionedIdentifier | None = None
