from requests import get
from bs4 import BeautifulSoup
#from file import save_to_file
from extractor.wwr import extra_wwr_jobs
from extractor.rok import extra_rok_jobs
from flask import Flask, render_template, request

app = Flask("JobScrapper")

@app.route("/")

def home():
  return render_template("index.html")

@app.route("/search")

def search():
  keyword = request.args.get("keyword")
  rok = extra_rok_jobs(keyword)
  wwr = extra_wwr_jobs(keyword)
  jobs = rok + wwr
  return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")

#keyword = input("What do you want to search for?")
#wwr = extra_wwr_jobs("python")
#rok = extra_rok_jobs("python")
#jobs = wwr + rok

#save_to_file(keyword, jobs)


#for job in jobs:
#  print(job)
#  print("################3")
