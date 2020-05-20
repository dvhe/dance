class Channel():
    async def send(self, content=None):
        return await self.client.api.send_message(self, content=content)