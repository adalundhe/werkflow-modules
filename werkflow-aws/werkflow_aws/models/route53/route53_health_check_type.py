from __future__ import annotations
from typing import Literal


Route53HealthCheckType = Literal[
    'HTTP',
    'HTTPS',
    'HTTP_STR_MATCH',
    'HTTPS_STR_MATCH',
    'TCP',
    'CALCULATED',
    'CLOUDWATCH_METRIC',
    'RECOVERY_CONTROL',
]
