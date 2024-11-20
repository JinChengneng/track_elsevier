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
    # Group events by revision first
    revision_timelines = {}
    
    for event in events:
        revision = event['Revision']
        reviewer_id = event['Id']
        
        if revision not in revision_timelines:
            revision_timelines[revision] = {}
            
        if reviewer_id not in revision_timelines[revision]:
            revision_timelines[revision][reviewer_id] = {
                'invited': None, 
                'accepted': None,
                'completed': None  # Add completed field
            }
        
        if event['Event'] == 'REVIEWER_INVITED':
            revision_timelines[revision][reviewer_id]['invited'] = event['Date']
        elif event['Event'] == 'REVIEWER_ACCEPTED':
            revision_timelines[revision][reviewer_id]['accepted'] = event['Date']
        elif event['Event'] == 'REVIEWER_COMPLETED':  # Add handling for completed event
            revision_timelines[revision][reviewer_id]['completed'] = event['Date']
    
    # Convert to structured format
    processed_timelines = []
    
    for revision, timeline in sorted(revision_timelines.items()):
        reviewer_list = [
            {
                'id': reviewer_id,
                'invited': data['invited'],
                'accepted': data['accepted'],
                'completed': data['completed']  # Add completed to output
            }
            for reviewer_id, data in timeline.items()
        ]
        
        # Sort reviewers by invited time and then by reviewer ID
        sorted_reviewers = sorted(
            reviewer_list,
            key=lambda x: (x['invited'] if x['invited'] is not None else float('inf'), x['id'])
        )
        
        processed_timelines.append({
            'revision': revision,
            'reviewers': sorted_reviewers
        })
    
    return processed_timelines