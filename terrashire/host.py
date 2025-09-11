'''
        "mac": "",
        "ip": "",
        "host": "",
        "description: "",
        "services": "",
        "password": "",
        "user": "",
        "ssh-key": ""
'''
import json
from paprika import *

@data
class Host:
    mac: str
    ip: str = ""
    host: str = ""
    description: str = ""
    services: str = ""  # Default value
    user: str = ""  
    password: str = "" 
    sshKey: str = ""

    @staticmethod
    def from_json_str(data):
        host = Host()
        print(data)
        # data = json.loads(s)

        host.mac = data["mac"]
        host.ip = data["ip"]
        host.services = data["services"]
        host.user = data["user"]
        host.password = data["password"]
        host.sshKey = data["sshKey"]
        host.host = data["host"]
        host.description = data["description"]

        return host
    
    def __repr__(self):
        """
        Overrides the default __repr__ method to provide a custom string
        representation for MyClass instances when pretty-printed.
        """
        return self.to_json_str()

    
    def toJSON(self):
        '''
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)
        '''
        return {
           "mac": self.mac,
           "ip": self.ip,
           "host": self.host,
           "description": self.description,
           "services": self.services,
           "user": self.user,
           "password": self.password,
           "sshKey": self.sshKey
        }

    def __str__(self):
        return self.to_json_str()

    def to_json_str(self):
        return json.dumps(self.toJSON(), indent=4)
