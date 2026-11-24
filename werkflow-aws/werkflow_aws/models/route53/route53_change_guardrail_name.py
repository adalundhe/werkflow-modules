from __future__ import annotations
from typing import Literal


Route53ChangeGuardrailName = Literal[
    'NS_FORMAT_CHECK',
    'NS_DELEGATION_AUTHORITY_CHECK',
    'NS_OCCLUSION_CHECK',
    'ALIAS_TARGET_CHECK',
    'ACTIVE_RECORD_CHECK',
    'ACTIVE_DELEGATION_CHECK',
]
