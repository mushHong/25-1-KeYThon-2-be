import requests
import json

press_dict = {
    "이데일리": "018",
    "매일신문": "088",
    "MBC": "214",
    "한국경제": "015",
    "YTN": "052",
    "머니투데이": "008",
    "경향신문": "032",
    "조선비즈": "366",
    "국민일보": "005",
    "조선일보": "023",
    "서울신문": "081",
    "중앙일보": "025",
    "강원일보": "087",
    "한국일보": "469",
    "미디어오늘": "006",
    "뉴스1": "421",
    "연합뉴스": "001",
    "연합뉴스TV": "422",
    "JTBC": "437",
    "서울경제": "011",
    "MBN": "057",
    "SBS": "055",
    "아이뉴스24": "031",
    "문화일보": "021",
    "데일리안": "119",
    "주간조선": "053",
    "코메디닷컴": "296",
    "매일경제": "009",
    "한겨레": "028",
    "헤럴드경제": "016",
    "파이낸셜뉴스": "014",
    "KBS": "056",
    "오마이뉴스": "047",
    "동아사이언스": "584",
    "노컷뉴스": "079",
    "채널A": "449",
    "아시아경제": "277",
    "세계일보": "022",
    "동아일보": "020",
    "비즈워치": "648",
    "더팩트": "629",
    "헬스조선": "346",
    "부산일보": "082",
    "조세일보": "123",
    "디지털타임스": "029",
    "뉴스타파": "607",
    "kbc광주방송": "660",
    "뉴시스": "003",
    "SBS Biz": "374",
    "한국경제TV": "215",
    "블로터": "293",
    "시사저널": "586",
    "전자신문": "030",
    "TV조선": "448",
    "디지털데일리": "138",
    "지디넷코리아": "092",
    "신동아": "262",
    "코리아헤럴드": "044",
    "기자협회보": "127",
    "농민신문": "662",
    "프레시안": "002",
    "한경비즈니스": "050",
    "경기일보": "666",
    "강원도민일보": "654",
    "월간 산": "094",
    "대전일보": "656",
    "매경이코노미": "024",
    "국제신문": "658",
    "시사IN": "308",
    "코리아중앙데일리": "640",
    "이코노미스트": "243",
    "머니S": "417",
    "여성신문": "310",
    "전주MBC": "659",
    "한겨레21": "036",
    "JIBS": "661",
    "주간경향": "033",
    "일다": "007",
    "대구MBC": "657",
    "주간동아": "037",
    "CJB청주방송": "655",
    "더스쿠프": "665",
    "중앙SUNDAY": "353",
    "레이디경향": "145"
}


# 네이버 API 인증 정보
CLIENT_ID = "bAH1YsUVJACd04LZpvmx"  # 발급받은 클라이언트 ID
CLIENT_SECRET = "QRde3I7aiD"  # 발급받은 클라이언트 시크릿


# API 요청 함수
def search_naver_news(query, display=10, start=1, sort="date"):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }
    params = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error Code: {response.status_code}")
        return None

def query_naver_link(query):
    urls = []
    descriptions = []
    titles = []
    
    query = "대통령"  # 검색어
    results = search_naver_news(query, sort="date")
    
    item = results['items']
    
    for i in range(len(item)):
        data = item[i]
        title = data['title']
        titles.append(title)
        des = data['description']
        descriptions.append(des)
        link = data['link']
        urls.append(link)
    
    return urls, descriptions, titles


# 테스트 실행
if __name__ == "__main__":
    query = "대통령"  # 검색어
    
    urls, descriptions, titles = query_naver_link(query)
    print(urls[0])
