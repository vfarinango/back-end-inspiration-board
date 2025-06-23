from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Card(db.Model):
    card_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int]

    @classmethod
    def from_dict(cls, card_data):
        return cls(
            message=card_data["message"],
            likes_count=card_data["likes_count"]
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count
        }
    # def update(self, data):
    #     if "title" in data:
    #         self.title = data["title"]