import mechanize
from bs4 import BeautifulSoup
import codecs
import getpass
driver = webdriver.Firefox()

USERNAME = str(raw_input("username: "))
PASSWORD = getpass.getpass("password:  ")


def htmlHandle(USERNAME, PASSWORD):

    url = 'https://my.olin.edu/ICS/My_StAR/My_Schedule_and_Registration_Info.jnz'

    viewdetails = "pg0_V_lnkView"
    driver.get(url)
    elem = driver.find_element_by_name('userName')
    elem.send_keys(USERNAME)
    elem = driver.find_element_by_name('password')
    elem.send_keys(PASSWORD)

    driver.find_element_by_id("btnLogin").click()


    driver.find_element_by_id(viewdetails).click()
    html = driver.page_source

    soup = BeautifulSoup(html)
    tabulka = soup.find(id = "pg0_V_ggCourses")
    tab = tabulka.find('tbody').findAll('tr')[0].findAll('td')[1].string

    Data = []

    for row in tabulka.find('tbody').findAll('tr'):
        times = []
        course = str(row.findAll('td')[1].string.strip())
        for li in row.findAll('td')[2].findAll('li'):
            times.append(str(li.string.strip()).replace("\r\n\t\t\t\t\t\t\t\t\t\t"," "))
        Data.append(course)
        Data.append(times)

    return Data

testfile =open('html.txt','w')

testfile.write(htmlHandle(USERNAME,PASSWORD))


'''
def htmlHandle(USERNAME, PASSWORD):

	url = 'https://my.olin.edu/ICS/My_StAR/My_Schedule_and_Registration_Info.jnz'

    viewdetails = "pg0_V_lnkView"
	br = mechanize.Browser()
	br.open(url)

	br.select_form(nr=0)
    

	br["userName"] = USERNAME
	br["password"] = PASSWORD
	html = str(br.submit().read())
    driver.find_element_by_id(viewdetails).click()
    html = driver.page_source

	soup = BeautifulSoup(html)

	tabulka = soup.find(id = "pg0_V_ggCourses")
	tab = tabulka.find('tbody').findAll('tr')[0].findAll('td')[1].string

	courseNames = []
	courseTimes = []

	for row in tabulka.find('tbody').findAll('tr'):
		times = []
		course = str(row.findAll('td')[1].string.strip())
		for li in row.findAll('td')[2].findAll('li'):
			times.append(str(li.string.strip()).replace("\r\n\t\t\t\t\t\t\t\t\t\t"," "))

		courseTimes.append(times)
		courseNames.append(course)

	courseLocations = []
	for i in range(len(courseNames)):
		courseLocations.append("Location feature not yet implemented")

	numOfCourses = str(len(courseNames))

	return [numOfCourses,courseNames,courseTimes,courseLocations]

def formatInfo(numOfCourses,courseNames,courseTimes,courseLocations):
	info = ""
	info += (numOfCourses + "\n")
	for i in range(int(numOfCourses)):
		info += (courseNames[i]+"\n")
		for j in range(len(courseTimes[i])):
			info += (str(courseTimes[i][j]) + "  ")
		info += ("\n")
		info += (courseLocations[i] + "\n")
	return info

htmlResults = htmlHandle(USERNAME,PASSWORD)

num = htmlResults[0]
names = htmlResults[1]
times = htmlResults[2]
locs = htmlResults[3]
'''
