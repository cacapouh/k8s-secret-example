import json

with open("/etc/config/credentials.json") as f:
    credentials = json.loads(f.read())

if __name__ == '__main__':
    user = credentials['user']
    password = credentials['password']
    print("{}:{}".format(user, password))
