from sqlalchemy import Column, Integer, Float, ForeignKey

from .database import Base


class Child(Base):
    __tablename__ = "children"
    ChildID: Column("child_id", Integer, primaray_key=True, index=True)
    GradeLevel: Column("grade_level", Integer, nullable=False)

class Submission(Base):
    """SQLAlchemy model to represent data that is stored in database
    for more information see:
    https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models
    """
    __tablename__ = "submissions"
    SubmissionID: Column("sub_id", Integer, primary_key=True, index=True)
    ChildID: Column("child_id", ForeignKey("children.child_id"))
    StoryID: Column("story_id", Integer, unique=False, nullable=False)
    StoryLength: Column("story_length", Integer)
    AverageWordLength: Column("avg_word_len", Float)
    NumberQuotes: Column("quotes_num", Integer)
    UniqueWordsNumber: Column("unique_words_num", Integer)
    AdjectiveNumber: Column("adj_num", Integer)
    SquadScore: Column("squad_score", Float)
