#import databases
from databases import Database
from sqlalchemy.dialects.postgresql import UUID,JSONB,BIGINT
from datetime import timezone
from sqlalchemy import (Boolean,Date,DateTime,Float,Integer,MetaData,Numeric,Table,Column,String,ARRAY,create_engine)
from settings import (POSTGRES_USERNAME,POSTGRES_PASSWORD,POSTGRES_SERVER,POSTGRES_SCHEMA)

DATABASE_URL=(f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}")
pg_database=Database(DATABASE_URL,ssl=True,min_size=2,max_size=10)
metadata=MetaData(schema=POSTGRES_SCHEMA)
tz_utc=timezone.utc

customer_table=Table("customer",
                     metadata,
                     Column("id",Integer,primary_key=True),
                     Column("name",String,primary_key=True),
                     Column("city",String,primary_key=True))


async def get_customer_details(id):
    customer_table.select().with_only_columns([
        customer_table.c.id.label("id"),
        customer_table.c.name.label("name"),
        customer_table.c.city.label("city")

    ]).where(customer_table.c.id==id)


