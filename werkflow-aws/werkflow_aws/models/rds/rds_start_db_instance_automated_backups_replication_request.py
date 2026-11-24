from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_tag_model import RDSTagModel


class RDSStartDBInstanceAutomatedBackupsReplicationRequest(BaseModel):
    SourceDBInstanceArn: StrictStr
    BackupRetentionPeriod: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
    SourceRegion: StrictStr | None = None
