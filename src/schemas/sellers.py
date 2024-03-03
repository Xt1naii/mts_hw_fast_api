from pydantic import BaseModel, EmailStr

from .books import ReturnedBook


__all__ = ["BaseSeller", "IncomingSeller", "ReturnedSeller", "ReturnedAllSellers", "ReturnedSellerBooks"]  # noqa


class BaseSeller(BaseModel):
    first_name: str
    last_name: str
    e_mail: EmailStr()


class IncomingSeller(BaseSeller):
    password: str


class ReturnedSeller(BaseSeller):
    id: int


class ReturnedAllSellers(BaseModel):
    sellers: list[ReturnedSeller]


class ReturnedSellerBooks(ReturnedSeller):
    books: list[ReturnedBook]
