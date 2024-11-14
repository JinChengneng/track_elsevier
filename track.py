import requests
from datetime import datetime

def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_manuscript_info(uuid):
    url = f"https://tnlkuelk67.execute-api.us-east-1.amazonaws.com/tracker/{uuid}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None

def process_review_timeline(events):
    timeline = {}
    for event in events:
        reviewer_id = event['Id']
        if reviewer_id not in timeline:
            timeline[reviewer_id] = {'invited': None, 'accepted': None}
        
        if event['Event'] == 'REVIEWER_INVITED':
            timeline[reviewer_id]['invited'] = event['Date']
        elif event['Event'] == 'REVIEWER_ACCEPTED':
            timeline[reviewer_id]['accepted'] = event['Date']
    
    # Convert to list of dictionaries
    timeline_list = [
        {
            'id': reviewer_id,
            'invited': data['invited'],
            'accepted': data['accepted']
        }
        for reviewer_id, data in timeline.items()
    ]
    
    # Sort by invited time and then by reviewer ID
    return sorted(timeline_list, 
                 key=lambda x: (x['invited'] if x['invited'] is not None else float('inf'), 
                              x['id']))