from pydantic import BaseModel
from typing import List
class ProductivityTips(BaseModel):
    tips: List[str]
    category: str
    priority: str
