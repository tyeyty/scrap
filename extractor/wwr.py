from requests import get
from bs4 import BeautifulSoup

def extra_wwr_jobs(keyword):

  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website")
  else:
    results = []
    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    #print(len(jobs))
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1) #delete view_all
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, kind, location = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        
        #print(post)
        #print(company.string, kind.string, region.string, title.string)
  
        job_data = {
          'company': company.string,
          #'kind': kind.string,
          'link': f"https://weworkremotely.com{link}",
          'location': location.string,
          'position': title.string
        }
        results.append(job_data)
  
    return results