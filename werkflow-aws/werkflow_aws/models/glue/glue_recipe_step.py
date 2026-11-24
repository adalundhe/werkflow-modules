from __future__ import annotations
from pydantic import BaseModel
from .glue_condition_expression import GlueConditionExpression
from .glue_recipe_action import GlueRecipeAction


class GlueRecipeStep(BaseModel):
    Action: GlueRecipeAction | None = None
    ConditionExpressions: list[GlueConditionExpression] | None = None
