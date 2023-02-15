from pydantic import BaseModel, EmailStr
from pydantic.types import PaymentCardNumber


class Owner(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr