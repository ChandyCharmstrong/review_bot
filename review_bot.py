import requests
import re

"""def post_google_review(google_maps_url, review_text, star_rating):
    # Remove leading/trailing spaces from the URL
    google_maps_url = google_maps_url.strip()

    # Extract Place ID from Google Maps URL
    query_part = google_maps_url.split('?')[1]  # Get the query part after the '?'
    query_params = query_part.split('&')        # Split the query parameters
    place_id_param = next((param for param in query_params if 'data=!3m1!4b1!4m6!3m5!1s' in param), None)
    if place_id_param:
        place_id = place_id_param.split('=')[1]
    else:
        print("Invalid Google Maps URL format.")
        return"""
        
def post_google_review(google_maps_url, review_text, star_rating):
    # Remove leading/trailing spaces from the URL
    google_maps_url = google_maps_url.strip()

    # Extract Place ID from Google Maps URL
    match = re.search(r'place/([^/]+)', google_maps_url)
    if match:
        place_id = match.group(1)
    else:
        print("Invalid Google Maps URL format.")
        return

    # Set up the review POST request
    review_url = f'https://www.google.com/maps/preview/review/render'
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    payload = {
        'ajax': '1',
        'ei': place_id,
        'm': '',
        'source': 'mobile',
        'json': '1',
        'authuser': '0',
        'gmid': '',
        'hl': 'en',
        'gl': 'us',
        'ceid': '',
        'x': '345',
        'iv': '',
    }

    # Fill in the review details
    payload['comment'] = review_text
    payload['star'] = str(star_rating)  # Convert to string

    # Send the review POST request
    response = requests.post(review_url, headers=headers, data=payload)

    # Check if the review was successfully submitted
    if response.status_code == 200:
        print("Review submitted successfully!")
    else:
        print("Failed to submit the review.")

# Example usage:
if __name__ == "__main__":
    google_maps_url = "https://www.google.com/maps/place/Queen+of+Hoxton/@51.5220971,-0.0811529,17z/data=!3m1!4b1!4m6!3m5!1s0x48761cb1cf4211b9:0x38d5358623731b26!8m2!3d51.5220971!4d-0.0811529!16s%2Fm%2F0lr46vf?entry=ttu"
    review_text = "This bar fine. The security team aren't very judicious though."
    star_rating = 3  # A value between 1 to 5

    post_google_review(google_maps_url, review_text, star_rating)
