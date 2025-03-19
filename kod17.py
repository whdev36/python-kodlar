# 🛠️ async va await kalit so‘zlari

import asyncio

async def salom():
    print("Salom, dunyo!")
    await asyncio.sleep(2)
    print("Asinxron dasturlashni o'rganamiz!")

# asyncio.run(salom())

# 🔄 Bir nechta funksiyalarni parallel bajarish:
async def vazifa(nom, vaqt):
    print(f"{nom} boshlandi ...")
    await asyncio.sleep(vaqt)
    print(f"{nom} tugadi ...")

async def main():
    await asyncio.gather(
        vazifa("⛏️ Data Parsing", 3),
        vazifa("📡 API so‘rovi", 2),
        vazifa("🔍 Ma'lumot qidirish", 1)
    )

# asyncio.run(main())

# 🛑 Asinxron kodni xatolar bilan ushlash:
async def xato_vazifa():
    raise ValueError('Xatolik yuz berdi!')

async def main():
    try:
        await xato_vazifa()
    except ValueError as e:
        print(f"Xato: {e}")

# asyncio.run(main())

# 🔥 Real hayotda asinxron API bilan ishlash:
import aiohttp

async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
        
async def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = await get_data(url)
    print(data)

# asyncio.run(main())

# 🚦 Asinxron for-sikl (async for):
# import asyncio

async def sanash():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

# asyncio.run(sanash())

# 🎁 BONUS: Ultimate Trick 🔥
async def teskari_sanash():
    for i in range(10, 0, -1):
        print(i)
        await asyncio.sleep(1)
    print("🚀 Start!")
asyncio.run(teskari_sanash())