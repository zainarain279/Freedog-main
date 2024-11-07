import requests
from urllib.parse import urlparse, parse_qs
import hashlib
import time

# Display custom ASCII banner
def display_banner():
    print("░▀▀█░█▀█░▀█▀░█▀█")
    print("░▄▀░░█▀█░░█░░█░█")
    print("░▀▀▀░▀░▀░▀▀▀░▀░▀")
    print("╔══════════════════════════════════╗")
    print("║                                  ║")
    print("║  ZAIN ARAIN                      ║")
    print("║  AUTO SCRIPT MASTER              ║")
    print("║                                  ║")
    print("║  JOIN TELEGRAM CHANNEL NOW!      ║")
    print("║  https://t.me/AirdropScript6     ║")
    print("║  @AirdropScript6 - OFFICIAL      ║")
    print("║  CHANNEL                         ║")
    print("║                                  ║")
    print("║  FAST - RELIABLE - SECURE        ║")
    print("║  SCRIPTS EXPERT                  ║")
    print("║                                  ║")
    print("╚══════════════════════════════════╝")

# Headers and other necessary components
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': '',
    'x-requested-with': 'org.telegram.messenger',
}

def compute_md5(amount, seq):
    prefix = str(amount) + str(seq) + "7be2a16a82054ee58398c5edb7ac4a5a"
    return hashlib.md5(prefix.encode()).hexdigest()

def auth(url: str) -> dict:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.fragment)
    init = query_params.get('tgWebAppData', [None])[0]
    params = {'invitationCode': '', 'initData': init}
    data = {'invitationCode': '', 'initData': init}
    response = requests.post('https://api.freedogs.bot/miniapps/api/user/telegram_auth', params=params, headers=headers, data=data)
    return response.json()

def do_click(init):
    headers['authorization'] = 'Bearer ' + auth(init)['data']['token']
    params = ''
    response = requests.get('https://api.freedogs.bot/miniapps/api/user_game_level/GetGameInfo', params=params, headers=headers)
    Seq = response.json()['data']['collectSeqNo']
    hsh = compute_md5('100000', Seq)
    params = {
        'collectAmount': '100000',
        'hashCode': hsh,
        'collectSeqNo': str(Seq),
    }
    response = requests.post('https://api.freedogs.bot/miniapps/api/user_game/collectCoin', params=params, headers=headers, data=params)
    return response.json()

if __name__ == '__main__':
    # Display banner first
    display_banner()

    # Main process
    result = do_click('Enter Your FreeFogs Session link ')
    print(result)
    time.sleep(160)

    # Loop for repeated clicks
    for _ in range(25):  # Adjust the count as needed
        result = do_click('Enter Your FreeFogs Session link ')
        print(result)
        time.sleep(160)