#TODO Remove hardcoded keywords if UI happens
KEYWORDS = [

'bash', 'python', 'java', 'c++', 'ruby', 'perl', 'matlab', 'javascript', 'scala', 'firmware'
'php', 'Sauce Labs', 'flask', 'shell', 'Telecom', 'NAS', 'SAN', 'iSCSI', 'scripts', 'scripting',
'junit', 'selenium', 'react', 'c#', 'TestRail', 'Confluence', 'JMeter',
'tableau', 'd3.js', 'sas', 'spss', 'd3', 'saas', 'pandas', 'numpy', 'Jenkins', 'scipy', 'plan', 'case',
'sps', 'spotfire', 'scikits.learn', 'splunk', 'h2o', 'jira', 'functional', 'integration', 'stress', 'load', 'performance',
'hadoop', 'mapreduce', 'spark', 'pig', 'hive', 'shark', 'oozie', 'zookeeper', 'flume', 'mahout',
'elasticsearch', 'api', 'Mockito', 'Robotium', 'frontend', 'backend',
'sql', 'nosql', 'hbase', 'cassandra', 'xml', 'rust', 'mongodb', 'mysql', 'mssql', 'postgre', 'oracle',
'rdbms', 'mobile', 'android', 'ios', 'cucumber', 'iot', 'black', 'white', 'telecommunications',
'hive', 'cucumber', 'aws', 'azure', 'amazon', 'google', 'rest', 'docker', 'container', 'puppet', 'chef',
'kubernetes', 'storage', 'network', 'networking', 'maven', 'ci', 'cd', 'ci/cd', 'gui', 'ui', 'scrapy', 'beautifulsoup',
'restassured', 'ios', 'json', 'swift', 'objective-c', 'groovy', '.net', 'angular', 'node.js', 'kafka', 'mesos',
'django', 'pytest', 'css', 'html', 'appium', 'linux', 'css', 'ui', 'soa', 'unix', 'RESTful', 'Elastic', 'git', 'github', 'database',
'acceptance', 'uat', 'healthcare', 'banking', 'rest',
]


TITLE_MATCH_THRESHOLD = 90

TITLES = {'software': 30, 'quality': 80, 'assurance': 90, 'qa': 100, 'sqa': 100, 'sdet': 100, 'test': 70, 'automation': 70, 'engineer': 20}




'''
 https://www.indeed.com/jobs?as_and=senior+technical+support+engineer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=fulltime&st=&as_src=&salary=145000&radius=100&l=San+Jose%2C+CA&fromage=15&limit=50&sort=&psf=advsrch

INDEED_ROOT_URL = 'https://www.indeed.com/jobs?'
INDEED_TITLE_QUERY_TERM = 'as_and'
INDEED_JOB_TYPE_QUERY_TERM = 'jt'  #fulltime, parttime . . .
INDEED_SALARY_QUERY_TERM = 'salary'
INDEED_DISTANCE_QUERY_TERM = 'radius'
INDEED_LOCATION_QUERY_TERM = 'l'
INDEED_JOB_DESCRIPTION_AGE_QUERY_TERM = 'fromage'
INDEED_LIST_LIMIT_QUERY_TERM = 'limit'
INDEED_ADVANCED_SERCH_INDICATOR = 'psf=advsrch'
INDEED_URL_TEMPATE = INDEED_ROOT_URL + INDEED_TITLE_QUERY_TERM + '={}&' + INDEED_JOB_TYPE_QUERY_TERM + '={}&' + INDEED_SALARY_QUERY_TERM + '={}&' + INDEED_DISTANCE_QUERY_TERM + '={}&' + INDEED_LOCATION_QUERY_TERM + '={}&' +  INDEED_JOB_DESCRIPTION_AGE_QUERY_TERM + '={}&' + INDEED_LIST_LIMIT_QUERY_TERM + '={}&' + INDEED_ADVANCED_SERCH_INDICATOR
'''
INDEED_URL_TEMPATE = 'https://www.indeed.com/jobs?as_and={}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt={}&st=&as_src=&salary={}&radius={}&l={}fromage={}&limit=500&sort=&psf=advsrch'
