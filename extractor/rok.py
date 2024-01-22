from requests import get
from bs4 import BeautifulSoup

def extra_rok_jobs(keyword):

  base_url = "https://remoteok.com/remote-"
  base_url_end = "-jobs"

  response = get(
    f"{base_url}{keyword}{base_url_end}",
    headers={
      "User-Agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    })

  if response.status_code != 200:
    print("Can't request website")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('tr', class_="job")
    #print(jobs)
    #jobs = job_body.find_all('tr', class_="job")
    for job_section in jobs:
      job_posts = job_section.find_all(
        'td', class_="company position company_and_position")
      #print(job_posts)
      #print("##############")

      for post in job_posts:
        title = post.find('h2', itemprop="title")
        company = post.find('h3', itemprop="name")
        location = post.find('div', class_="location")
        link = post.find('a')
        job_data = {
          'company': company.string,
          'link': f"https://remoteok.com/{link['href']}",
          'location': location.string,
          'position': title.string
        }
        results.append(job_data)
        #print(title.string, company.string, location.string)

    return results
