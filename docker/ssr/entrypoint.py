import json
import os

protocol_param = os.getenv('SSR_PROTOCOL_PARAM')
obfs_param = os.getenv('SSR_OBFS_PARAM')
f = open('/etc/shadowsocksr/config.json', 'r+', encoding='utf-8')
jobj = json.load(f)
jobj['server'] = os.getenv('SSR_SERVER')
jobj['server_port'] = int(os.getenv('SSR_SERVER_PORT'))
jobj['password'] = os.getenv('SSR_PASSWORD')
jobj['method'] = os.getenv('SSR_METHOD')
jobj['protocol'] = os.getenv('SSR_PROTOCOL')
jobj['protocol_param'] = protocol_param if protocol_param else ''
jobj['obfs'] = os.getenv('SSR_OBFS')
jobj['obfs_param'] = obfs_param if obfs_param else ''
print(json.dumps(jobj, indent=4))
f.seek(0)
json.dump(jobj, f, indent=4)