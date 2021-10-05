from sqlalchemy import create_engine, MetaData, engine

engine = create_engine('mysql+pymysql://duck:@localhost:3306/fastapi_crud')
meta = MetaData()
conn = engine.connect()