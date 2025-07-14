from typing import Literal

MSKEnhancedMonitoring = Literal[
    'DEFAULT',
    'PER_BROKER',
    'PER_TOPIC_PER_BROKER',
    'PER_TOPIC_PER_PARTITION',
]