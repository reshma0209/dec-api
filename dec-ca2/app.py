from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def display_posts():
   try:
       url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile-by-salesnavurl?linkedin_url=https%3A%2F%2Fwww.linkedin.com%2Fsales%2Flead%2FACoAAABD0a4B2wblfHunfjGEN-uRLdg2MnWydmk%2Cname%2Czofi&include_skills=false&include_certifications=false&include_publications=false&include_honors=false&include_volunteers=false&include_projects=false&include_patents=false&include_courses=false&include_organizations=false"
       #querystring = {"username": "adamselipsky"}
       '''
       querystring = {
            "include_skills": "true",
            "include_certifications": "true",
            "include_publications": "false"
        }
        '''
       headers = {
            'x-rapidapi-key': "44ea5782b6mshfc5d9605f874bf9p1d40cdjsn001f5a24f788",
            'x-rapidapi-host': "fresh-linkedin-profile-data.p.rapidapi.com"
       }


       #response = requests.get(url, headers=headers, params=querystring)
       response = requests.get(url, headers=headers)
       response.raise_for_status()
       posts_data = response.json()
       #print(posts_data)
       # If the API returns a list directly
       if isinstance(posts_data, list):
           posts = posts_data
       # If the API wraps posts in a 'data' key
       elif isinstance(posts_data, dict) and 'data' in posts_data:
           posts = posts_data['data']
       else:
           posts = []


       return render_template('index.html', posts=posts)
  
   except requests.exceptions.RequestException as e:
       return render_template('index.html', posts=[], error=str(e))


if __name__ == '__main__':
   app.run(debug=True,port=5001)