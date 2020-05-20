class Message():
    def __init__(self, client, data=None):
        self.client = client
        # self.author = self.client.users.get(author_id)

    def reply(self, content):
        return self.channel.send(content)