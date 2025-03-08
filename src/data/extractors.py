import requests

def extract_data_from_serper(query, api_key):
    url = f"https://api.serper.dev/search"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        "q": query,
        "num": 10
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data from SERPER API: {response.status_code} - {response.text}")

def iterative_query_refinement(initial_query, api_key, iterations=3):
    refined_query = initial_query
    results = []
    
    for _ in range(iterations):
        data = extract_data_from_serper(refined_query, api_key)
        results.append(data)
        
        # Implement logic for refining the query based on the results
        # For example, you might want to adjust the query based on the first result's title or snippet
        if data['organic_results']:
            refined_query = data['organic_results'][0]['title']  # Example refinement
    
    return results