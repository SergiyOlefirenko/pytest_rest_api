from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color

from src.enums.computer_enums import Statuses
from src.pydantic_schemas.detailed_info import DetailedInfo

class Computer(BaseModel):

    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


if __name__ == '__main__':
    from src.pydantic_schemas.comp_example import computer
    comp = Computer.parse_obj(computer)
    json_str = comp.json()
    print(comp)
    print()
    print(json_str)
    print(comp.schema_json())