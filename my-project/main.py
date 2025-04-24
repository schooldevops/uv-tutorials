import requests
from typing import Dict, Any


def fetch_webpage(url: str) -> str:
    """
    웹 페이지의 내용을 가져옵니다.
    
    Args:
        url: 가져올 웹 페이지의 URL
        
    Returns:
        웹 페이지의 HTML 내용
    """
    response = requests.get(url)
    response.raise_for_status()  # 오류가 있으면 예외 발생
    return response.text


def get_json_data(url: str) -> Dict[str, Any]:
    """
    JSON API에서 데이터를 가져옵니다.
    
    Args:
        url: JSON API의 URL
        
    Returns:
        JSON 응답 데이터
    """
    response = requests.get(url, headers={"Accept": "application/json"})
    response.raise_for_status()
    return response.json()


def main():
    try:
        # 웹 페이지 크롤링 예제
        html_content = fetch_webpage("https://example.com")
        print(f"웹 페이지 크롤링 성공! 내용 일부: {html_content[:100]}...")
        
        # JSON API 호출 예제
        json_data = get_json_data("https://jsonplaceholder.typicode.com/posts/1")
        print(f"JSON 데이터 가져오기 성공!")
        print(f"제목: {json_data.get('title')}")
        print(f"내용: {json_data.get('body')[:50]}...")
        
    except requests.RequestException as e:
        print(f"요청 중 오류 발생: {e}")


if __name__ == "__main__":
    main()
