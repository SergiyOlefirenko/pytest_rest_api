from pydantic import BaseModel
from pydantic.types import List

from src.pydantic_schemas.owner import Owner
from src.pydantic_schemas.physical import Physical

class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owner]
