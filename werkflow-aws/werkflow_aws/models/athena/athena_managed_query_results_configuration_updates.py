from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .athena_managed_query_results_encryption_configuration import AthenaManagedQueryResultsEncryptionConfiguration


class AthenaManagedQueryResultsConfigurationUpdates(BaseModel):
    Enabled: StrictBool | None = None
    EncryptionConfiguration: AthenaManagedQueryResultsEncryptionConfiguration | None = None
    RemoveEncryptionConfiguration: StrictBool | None = None
