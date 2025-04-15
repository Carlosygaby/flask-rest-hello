from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_body: Mapped[str] = mapped_column(String(600), nullable=False)
    autor_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

    def serialize_comment(self):
        return {
            "id": self.id,
            "comment_body": self.comment_body,
            "autor_id": self.autor_id,
            "post_id": self.post_id,
        }


class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

    def serialize_post(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }


class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(200), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

    def serialize_Media(self):
        return {
            "id": self.id,
            "url": self.url,
            "post_id": self.post_id
        }


class Followers(db.Model):
    __tablename__ = 'followers'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)
    user_to_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)

    def serialize_followers(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }
