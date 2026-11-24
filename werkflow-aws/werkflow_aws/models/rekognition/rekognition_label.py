from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .rekognition_instance import RekognitionInstance
from .rekognition_label_alias import RekognitionLabelAlias
from .rekognition_label_category import RekognitionLabelCategory
from .rekognition_parent import RekognitionParent


class RekognitionLabel(BaseModel):
    Name: StrictStr | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Instances: list[RekognitionInstance] | None = None
    Parents: list[RekognitionParent] | None = None
    Aliases: list[RekognitionLabelAlias] | None = None
    Categories: list[RekognitionLabelCategory] | None = None
