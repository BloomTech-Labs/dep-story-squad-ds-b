from sqlalchemy import Column, Integer, Float

from .database import Base


class Submission(Base):
    __tablename__ = "submissions"
    SubmissionID: Column("sub_id", Integer, primary_key=True, index=True)
    CohortID: Column("cohort_id", Integer, nullable=True)
    StoryID: Column("story_id", Integer, unique=False, nullable=False)
    StoryLength: Column("story_length", Integer)
    AverageWordLength: Column("avg_word_len", Float)
    NumberQuotes: Column("quotes_num", Integer)
    UniqueWordsNumber: Column("unique_words_num", Integer)
    AdjectiveNumber: Column("adj_num", Integer)
    SquadScore: Column("squad_score", Float)
