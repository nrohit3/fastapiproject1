#import databases
from databases import Database
from sqlalchemy.dialects.postgresql import UUID,JSONB,BIGINT
from datetime import timezone
from sqlalchemy import (Boolean,Date,DateTime,Float,Integer,MetaData,Numeric,Table,Column,String,ARRAY,create_engine)
from settings import (POSTGRES_USERNAME,POSTGRES_PASSWORD,POSTGRES_SERVER,POSTGRES_SCHEMA)

DATABASE_URL=(f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}")
pg_database=Database(DATABASE_URL,ssl=True,min_size=2,max_size=10)

print("Works fine")




