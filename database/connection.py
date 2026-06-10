from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://admin:admin123@127.0.0.1:5433/business_intelligence"
)

print("Database connection established.")