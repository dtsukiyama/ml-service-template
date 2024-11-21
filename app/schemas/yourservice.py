"""Schema for your service."""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import datetime


class ExampleSchema(BaseModel):
    """Schema example."""

    company_id: int
    name: str
    item_names: List[str]
