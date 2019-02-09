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


INDEED_URL_TEMPATE = 'https://www.indeed.com/jobs?as_and={}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt={}&st=&as_src=&salary={}&radius={}&l={}fromage={}&limit=500&sort=&psf=advsrch'
# https://www.indeed.com/jobs?as_and=senior+technical+support+engineer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=fulltime&st=&as_src=&salary=145000&radius=100&l=San+Jose,+CA&fromage=300&limit=50&sort=&psf=advsrch
INDEED_TITLE_ONLY_TEMPLATE = 'https://www.indeed.com/q-{}.html' #dash separated title text such as data-science-engineer
INDEED_JD_LINK_FINDERS = ['a', "jobtitle turnstileLink"]
