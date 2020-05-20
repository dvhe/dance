import asks
import json
import socketio

class HttpClient():
    def __init__(self, client):
        self.client = client
        self.token = client.token
        self.retries = 5
        self.endpoint = 'https://supertiger.tk/api'
        
        headers = {
            'authorization': self.token,
            'Content-Type': 'application/json;charset=utf-8'
        }

        self.session = asks.Session(headers=headers)

        def __del__(self):
            pass

        async def get(self, endpoint, **kwargs):
            return await self.request('GET', endpoint, **kwargs)

        async def put(self, endpoint, **kwargs):
            return await self.request('PUT', endpoint, **kwargs)

        async def post(self, endpoint, **kwargs):
            return await self.request('POST', endpoint, **kwargs)

        async def patch(self, endpoint, **kwargs):
            return await self.request('PATCH', endpoint, **kwargs)

        async def delete(self, endpoint, **kwargs):
            return await self.request('DELETE', endpoint, **kwargs)           

        async def request(self, method, endpoint, **kwargs):
            method = method
            endpoint = self.endpoint

            token = self.token
            if self.token is not None:
                headers['authorization'] = token

            data = kwargs.get('data')
            if data is not None:
                if isinstance(data, dict):
                    data = json.dumps(data)
                if isinstance(data, str):
                    data = data.encode('utf-8')

                headers['Content-Type'] = 'application/json;charset=utf-8'

            _json = kwargs.get('json')

            await self.session.request(method, endpoint, headers=headers, data=data, json=_json)

        async def send_message(self, channel, **kwargs):
            route = f"/messages/channels/{channel}"

            payload = {
                'message': kwargs.get('message')
            }

            await self.post(route, data=payload)

        def delete_message(self, channel, message):
            route = f"/messages/{message}/channels/{channel}"
            return self.delete(route)

        def edit_message(self, channel, message, **kwargs):
            route = f"/messages/{message}/channels/{channel}"
            
            payload = {
                'message': kwargs.get('message')
            }

            return self.patch(route, data=payload)

        def get_invites(self, server):
            return self.get(f"/servers/{server}/invites")

        def delete_invite(self, server, invite):
            return self.delete(f"/servers/{server}/invites/{invite}")

        def create_role(self, server, **fields):
            return self.post(f"/servers/{server}/roles", json=fields)

        def edit_role(self, server, role, **fields):
            route = f"/servers/{server}/roles/{role}"
            keys = ('name', 'permissions', 'deleteable', 'color')
            payload = {
                k: v for k, v in fields.itmes() if k in keys
            }
            return self.patch(route, json=payload)

        def delete_role(self, server, role):
            return self.delete(f"/servers/{server}/roles/{role}")

        def add_role(self, server, member, role):
            return self.patch(f"/servers/{server}/members/{member}/roles/{role}")

        def remove_role(self, server, member, role):
            return self.delete(f"/servers/{server}/members/{member}/roles/{role}")            

        def create_channel(self, server, **fields):
            return self.put(f"/servers/{server}/channels", json=fields)

        def delete_channel(self, channel):
            return self.delete(f"/servers/{server}/channels/{channel}")
        
        def send_typing(self, server, channel):
            return self.post(f"/channels/{channel}/typing")