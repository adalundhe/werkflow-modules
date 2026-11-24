from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSKafkaSettings(BaseModel):
    Broker: StrictStr | None = None
    Topic: StrictStr | None = None
    MessageFormat: StrictStr | None = None
    IncludeTransactionDetails: StrictBool | None = None
    IncludePartitionValue: StrictBool | None = None
    PartitionIncludeSchemaTable: StrictBool | None = None
    IncludeTableAlterOperations: StrictBool | None = None
    IncludeControlDetails: StrictBool | None = None
    MessageMaxBytes: StrictInt | None = None
    IncludeNullAndEmpty: StrictBool | None = None
    SecurityProtocol: StrictStr | None = None
    SslClientCertificateArn: StrictStr | None = None
    SslClientKeyArn: StrictStr | None = None
    SslClientKeyPassword: StrictStr | None = None
    SslCaCertificateArn: StrictStr | None = None
    SaslUsername: StrictStr | None = None
    SaslPassword: StrictStr | None = None
    NoHexPrefix: StrictBool | None = None
    SaslMechanism: StrictStr | None = None
    SslEndpointIdentificationAlgorithm: StrictStr | None = None
    UseLargeIntegerValue: StrictBool | None = None
