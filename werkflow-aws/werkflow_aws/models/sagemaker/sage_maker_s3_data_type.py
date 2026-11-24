from __future__ import annotations
from typing import Literal


SageMakerS3DataType = Literal[
    'ManifestFile',
    'S3Prefix',
    'AugmentedManifestFile',
    'Converse',
]
