import os
import uuid
import models

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# load environment variables
load_dotenv()
CLUSTER_USERNAME = os.environ['CLUSTER_USERNAME']
CLUSTER_PASSWORD = os.environ['CLUSTER_PASSWORD']

engine = create_engine(
    url=f'cockroachdb://{CLUSTER_USERNAME}:{CLUSTER_PASSWORD}@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dmild-walrus-2804'
)
session = sessionmaker(bind=engine)

def create_account(username: str, password: str):
    """CREATE AND REGISTER NEW ACCOUNT"""
    new_account = models.Account(
        id=uuid.uuid4(),
        username=username,
        password=password
    )

    global session
    session.add(new_account)

print(session)
conn = engine.connect(close_with_result=True)
print(conn.execute(statement='SHOW TABLES'))
