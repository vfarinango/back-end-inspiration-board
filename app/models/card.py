from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Card(db.Model):
    card_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey("board.board_id"), nullable=False)
    board: Mapped["Board"] = relationship(back_populates="cards")


    @classmethod
    def from_dict(cls, card_data):
        return cls(
            message=card_data["message"],
            likes_count=card_data["likes_count"],
            board_id=card_data["board_id"] 
        )
    
    def to_dict(self):
        return {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count,
            "board_id": self.board_id
        }
    # def update(self, data):
    #     if "title" in data:
    #         self.title = data["title"]