# 🔹 1. SQLite bilan ishlash (sqlite3)
# 📌 Bazaga ulanish va jadval yaratish:
import sqlite3

# 🛢️ Bazaga ulanish (yo‘q bo‘lsa, yaratadi)
conn = sqlite3.connect("users.db")

# 📝 Kursor yaratish (bazaga buyruqlar yuborish uchun)
cur = conn.cursor()

# 📌 Jadval yaratish
cur.execute("""
create table if not exists users (
            id integer primary key autoincrement,
            name text not null,
            age integer
        )
""")

# 🔄 O‘zgarishlarni saqlash
# conn.commit()
# conn.close()

# 📌 Ma’lumot qo‘shish

# 👤 Foydalanuvchini qo‘shish
# cur.execute('insert into users (name, age) values (?, ?)', ('Ali', 25))
# conn.commit()
# conn.close()

# 📌 Ma’lumotlarni olish
cur.execute('select * from users')
users = cur.fetchall()

for user in users:
    print(user)

# conn.close()

# 📌 Ma’lumotni yangilash
cur.execute('update users set age = 26 where name = "Ali"')
# conn.commit()

# 📌 Ma’lumotni o‘chirish
cur.execute('delete from users where name = "Ali"')
# conn.commit()
# conn.close()

# 🔹 2. SQLAlchemy bilan ishlash
# 📌 Bazaga ulanish va jadval yaratish

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 🛢️ Bazaga ulanish
engine = create_engine('sqlite:///users2.db')
Base = declarative_base()

# 📌 Jadval yaratish
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

Base.metadata.create_all(engine)

# 🎯 Session yaratish
Session = sessionmaker(bind=engine)
session = Session()

# # 📌 Foydalanuvchi qo‘shish
# new_user = User(name='Ali', age=25)
# session.add(new_user)
# session.commit()

# 📌 Ma’lumotlarni olish
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# # 📌 Ma’lumotni yangilash
# user = session.query(User).filter_by(name='Ali').first()
# user.age = 26
# session.commit()

# # 📌 Ma’lumotni o‘chirish
# user = session.query(User).filter_by(name='Ali').first()
# session.delete(user)
# session.commit()