from typing import Optional
import psycopg2
from sqlmodel import Field, Session, SQLModel, create_engine


class Website(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    website_name: str
    website_url: str
    website_type: Field(nullable=True)
    website_sitemap: str
    agent_name: Field(nullable=True)
    agent_instructions: Field(nullable=True)


#name = 'intimatehygine'
#url = 'https://intimatehygine.com/'
#sitemap = 'https://intimatehygine.com/sitemap_index.xml'

website_data = Website(website_name='intimatehygine', website_url='https://intimatehygine.com/', website_sitemap='https://intimatehygine.com/sitemap_index.xml')

engine = create_engine("postgresql+psycopg2://postgres:0203@localhost:5432/chatbot", echo=True)

SQLModel.metadata.create_all(engine)
with Session(engine) as session:
    session.add(website_data)
    session.commit()
