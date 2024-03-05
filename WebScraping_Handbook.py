import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Started Execution!!")


url = "https://hbook.westernsydney.edu.au/"
# url = "https://hbook.westernsydney.edu.au/subject-search/"

website = requests.get(url).text
soup = BeautifulSoup(website, "html.parser")

#fetch all the programs and cdms programs
program_lists = soup.find_all("ul", {"id": "/programs/"})
program_lists = program_lists[0]
programs=[]
cdms_programs=[]

for item in program_lists:
    if(item.get_text()!='\n'):
        anchor_element = item.find('a')
        url="https://hbook.westernsydney.edu.au"+anchor_element.get('href')
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        program_advice=soup.find_all("a", {"href": "mailto:CDMS@westernsydney.edu.au"})
        if(len(program_advice)!=0):
            cdms_programs.append(item.get_text())
        programs.append(item.get_text())


df = pd.DataFrame(cdms_programs, columns=["Programs"]) 
df.to_excel("cdms_programs.xlsx", index=False) 

df = pd.DataFrame(programs, columns=["Programs"]) 
df.to_excel("programs.xlsx", index=False) 

#Fetch all the majors and minors
majors_minors_lists = soup.find_all("ul", {"id": "/majors-minors/"})
majors_minors_lists = majors_minors_lists[0]
majors_minors=[]
cdms_majors_minors =[]

for item in majors_minors_lists:
    if(item.get_text()!='\n'):
        anchor_element = item.find('a')
        url="https://hbook.westernsydney.edu.au"+anchor_element.get('href')
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        program_advice=soup.find_all("a", {"href": "mailto:CDMS@westernsydney.edu.au"})
        if(len(program_advice)!=0):
            cdms_majors_minors.append(item.get_text())
        majors_minors.append(item.get_text())

df = pd.DataFrame(cdms_majors_minors, columns=["Majors&Minors"]) 
df.to_excel("cdms_majors_minors.xlsx", index=False) 

df = pd.DataFrame(majors_minors, columns=["Majors&Minors"]) 
df.to_excel("majors_minors.xlsx", index=False) 

#Fetch all the subjects
subject_lists = soup.find_all("ul", {"id": "/subject-details/"})
subject_lists = subject_lists[0]
all_subjects=[]
# urls=[]

for item in subject_lists:
    if(item.get_text()!='\n'):
        subject=item.get_text().split(" ")
        subject_code = subject[0]+subject[1]
        # urls.append("https://hbook.westernsydney.edu.au/subject-details/"+subject_code+"/")
        all_subjects.append(item.get_text())

df = pd.DataFrame({"All Subjects":all_subjects}) 
df.to_excel("subjects.xlsx", index=False) 


#Fetch CDMS subjects
with open('C:/Users/ASUS/ICTPracticum/handbook_subjects.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

subject_code_lists = soup.find_all("span", {"class": "result__code"})
subject_title_lists = soup.find_all("span", {"class": "result__title"})

subject_code=[]
for item in subject_code_lists:
    if(item.get_text()!='\n'):
        subject_code.append(item.get_text())

cdms_subjects=[]
for item in subject_title_lists:
    if(item.get_text()!='\n'):
        cdms_subjects.append(item.get_text())

df = pd.DataFrame({"Subject Code":subject_code,"Subject Title":cdms_subjects}) 
df.to_excel("cdms_subjects.xlsx", index=False)

print("Finished Execution!!")
