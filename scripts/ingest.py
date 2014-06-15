import urllib2
import json
import csv
import time


def get_job_page(url):
	req = urllib2.Request(url)
	req.add_header('Authorization', 'bearer c50f0129-3d40-4de5-99e8-c00410421a2e')
	job = json.loads(urllib2.urlopen(req).read())
	return job

if __name__ == "__main__":

	with open('all_jobs_data.csv', 'w') as of:
	#w = csv.writer(open("output.csv", "w"))
		for pagenum in range(100):
			time.sleep(1) # delays for 5 seconds
			print "------page : " + str(pagenum)
			url = 'https://api.dice.com/jobs?*=&count=120&page=' + str(pagenum+500)
			page = get_job_page(url)
			for job in page['searchResults']:
				j = {}
				j['id'] = str(job.get('id',''))
				j['areaCodeText'] = job.get('areaCodeText','')
				j['webUrl'] = job.get('webUrl','')
				j['telecommuteOption'] = job.get('telecommuteOption','')
				j['jobLength'] = job.get('jobLength','')
				j['postedDate'] = job.get('postedDate', '')
				j['freshnessDate'] = job.get('freshnessDate', '')
				j['creationDate'] = job.get('creationDate', '')
				j['firstActiveDate'] = job.get('firstActiveDate', '')
				j['skills'] = job.get('skills', '')
				j['payRate'] = job.get('payRate', '')
				j['taxTerms'] = job.get('taxTerms', '')
				j['travelRequiredMiles'] = job.get('travelRequiredMiles', '')
				#j['description'] = job.get('description', '')

				company = job['company']
				j['href'] = company.get('name', '')
				j['compURL'] = company.get('compURL','')
				j['name'] = company.get('name', '')

				position = job['position']
				j['title'] = job.get('title', '')

				location = position['location']
				j['country'] = location.get('country', '')
				j['city'] = location.get('city', '')
				j['region'] = location.get('region', '')
				j['postalCode'] = location.get('postalCode', '')

				of.write(str(j))
				of.write('\n')
					#of.write('\n')
				#for key, val in j.items():
				#	w.writerow([key, val])
				#json.dumps(j)
			#print("%s,%s,%s,%s,%s" % ()),
			#print("%s,%s" % (company.get('name',''), company.get('compURL',''))),
			#print("%(id)s,%(areaCodeText)s,%(webUrl)s,%(telecommuteOption)s" % job),	#%(jobLength)s,
			#print("%(name)s,%(compURL)s" % job['company']),
			
			#print("%s" % position.get('title', '')),
			#rint("%(title)s" % job['position']),
			
			#print("%s,%s,%s,%s" % (location.get('country', ''), location.get('city', ''), location.get('region', ''), location.get('postalCode', '')))
			#rint("%(country)s,%(city)s,%(region)s,%(postalCode)s" % job['position']['location'])

	#with open('tmp', 'r') as f:
	#	for line in f.readlines():
	#		#print line
	#		t = json.loads(line.strip())
	#		print t['id']
