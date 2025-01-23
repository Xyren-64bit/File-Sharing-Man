from bot import Bot

if __name__ == "__main__":
    bot = Bot()

    try:
        # Menjalankan bot
        bot.run()

        # Logika tambahan untuk Pyrogram
        async def process_dialogs(bot):
            async with bot.client as app:  # Pastikan bot memiliki atribut `client` (instance `Client`)
                try:
                    # Mendapatkan semua dialog
                    async for dialog in app.get_dialogs():
                        print(f"Dialog ditemukan: {dialog.chat.title if dialog.chat else 'Tidak diketahui'}")
                    
                    # Menyimpan state aplikasi
                    await app.storage.save()
                    print("State aplikasi berhasil disimpan.")
                
                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Kesalahan tak terduga: {e}")
        
        # Memulai proses async
        import asyncio
        asyncio.run(process_dialogs(bot))

    except Exception as e:
        print(f"Kesalahan saat menjalankan bot: {e}")
