from __future__ import annotations
from typing import Literal


LambdaKafkaSchemaRegistryAuthType = Literal[
    'BASIC_AUTH',
    'CLIENT_CERTIFICATE_TLS_AUTH',
    'SERVER_ROOT_CA_CERTIFICATE',
    'OAUTHBEARER_AUTH',
]
