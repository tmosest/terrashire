'''
{
    "servers": [{
        "mac": "",
        "ip": "",
        "services": "",
        "password": "",
        "user": "",
        "ssh-key": ""
    }],

    "router": {"service": "opnsense"},
    "proxy": { "service" : "proxy"}
}
'''
import json
import os
from paprika import *

from .host import Host

@data
class Config:
    servers: list
    servers_map: dict

    @staticmethod
    def loadConfig():
        json_file_name = ".Config.json" 
        json_file_name = os.getcwd() + '/' + json_file_name
        try:
            # Open the JSON file in read mode ('r')
            with open(json_file_name, 'r') as file:
                # Load the JSON data from the file into a Python dictionary
                data = json.load(file)
            
            # Now 'data' contains the content of your JSON file as a Python dictionary
            print("JSON data loaded successfully:")
            print(data)

            # You can access elements like a dictionary
            # Example: if your JSON has a key "name"
            # if "name" in data:
            #     print(f"Name: {data['name']}")
            config = Config()
            config.servers = [Host.from_json_str(s) for s in data["servers"]]
            
            config.servers_map = {}
            for server in config.servers:
                config.servers_map[server.mac] = server

            print(config.servers_map)

            return config

        except FileNotFoundError:
            print(f"Error: The file '{json_file_name}' was not found in the current directory.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{json_file_name}'. Ensure it's a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
