from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictBytes, StrictStr
from .aws_secrets_manager_replica_region import AWSSecretsManagerReplicaRegion
from .aws_secrets_manager_tag import AWSSecretsManagerTag


class AWSSecretsManagerCreateSecretRequest(BaseModel):
    Name: StrictStr
    ClientRequestToken: StrictStr | None = None
    Description: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    SecretBinary: StrictBytes | None = None
    SecretString: StrictStr | None = None
    Tags: list[AWSSecretsManagerTag] | None = None
    AddReplicaRegions: list[AWSSecretsManagerReplicaRegion] | None = None
    ForceOverwriteReplicaSecret: StrictBool | None = None
