import urllib.request
import json

HEADER_USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}

def get_target_api_url(page_number):
    return f"https://reqres.in/api/users?page={page_number}"

def get_request_object(page_number):
    req = urllib.request.Request(
        get_target_api_url(page_number),
        headers=HEADER_USER_AGENT    
    )
    return req

def request_users(users, page_number=1):
    req = get_request_object(page_number)
    with urllib.request.urlopen(req) as f:
        data_json = json.loads(f.read().decode('utf-8'))

        if page_number == 1:
            global total_pages
            total_pages = data_json['total_pages']

        for d in data_json['data']:
            users[d['id']] = f"{d['first_name']} {d['last_name']}"

def get_user_full_name_list(start, end):
    pass

if __name__ == "__main__":
    users = {} # {id, full_name}
    request_users(users)
    for i in range(total_pages, total_pages + 1):
        request_users(users, i)
    print(users)


