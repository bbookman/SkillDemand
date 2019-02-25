SUPERFLOUS_STRINGS = ['senior', 'director', 'manager', 'lead', 'mobile', 'sr', 'jr', 'I', 'II', 'III', 'IV','V' ,'(', ')', '.', ',', '/', '\\', "\'", '\"', '-',]


SKILL_KEYWORDS_QA =['bash', 'python', 'java', 'c++', 'ruby', 'perl', 'matlab', 'javascript', 'scala', 'firmware',
                 'php', 'Sauce Labs', 'flask', 'shell', 'Telecom', 'NAS', 'SAN', 'iSCSI', 'scripts', 'scripting',
                 'junit', 'selenium', 'react', 'c#', 'TestRail', 'Confluence', 'JMeter',
                'tableau', 'd3.js', 'sas', 'spss', 'd3', 'saas', 'pandas', 'numpy', 'Jenkins', 'scipy', 'plan', 'case',
                'sps', 'spotfire', 'scikits.learn', 'splunk', 'h2o', 'jira', 'functional', 'integration', 'stress', 'load', 'performance',
                'hadoop', 'mapreduce', 'spark', 'pig', 'hive', 'shark', 'oozie', 'zookeeper', 'flume', 'mahout',
                'elasticsearch', 'api', 'Mockito', 'Robotium', 'frontend', 'backend',
              'sql', 'nosql', 'hbase', 'cassandra', 'xml', 'rust', 'mongodb', 'mysql', 'mssql', 'postgre', 'oracle',
             'rdbms', 'mobile', 'android', 'ios', 'cucumber', 'iot', 'black', 'white', 'telecommunications',
             'hive', 'cucumber', 'aws', 'azure', 'amazon', 'google', 'rest', 'docker', 'container', 'puppet', 'chef',
             'kubernetes', 'storage', 'network', 'networking', 'maven', 'ci', 'cd', 'ci/cd', 'gui',
            'restassured', 'ios', 'json', 'swift', 'objective-c', 'groovy', '.net', 'angular', 'node.js', 'kafka', 'mesos',
            'django', 'pytest', 'css', 'html', 'appium', 'linux', 'css', 'ui', 'soa', 'unix', 'RESTful', 'Elastic', 'git',
            'github', 'database', 'acceptance', 'uat', 'healthcare', 'banking']


SITES_DICT = {

    'indeed' :{
        'url_template' : 'https://www.indeed.com/jobs?as_and={title}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&st=&as_src=&salary={salary}&radius={radius}&l={zipcode}&fromage={age}&limit=500&sort=&psf=advsrch',
        'title_selector' : 'turnstileLink',
        'title_word_sep': '+',
        'body_selector': 'body'
    },
    'careerbuilder' : {
        'url_template' : 'https://www.careerbuilder.com/jobs-{cbtitle}-in-{zipcode}?keywords={title}&location={zipcode}&radius={radius}&pay={salary}&posted={age}',
        'title_selector' : "//h2[@class='job-title show-for-medium-up']//a[@data-gtm='jrp-job-list|job-title-click|{}']",
        'title_word_sep': '+',
        'body_selector': 'body'

    },
    'monster':{
        'url_template' : 'https://www.monster.com/jobs/search/?q={title}&rad={radius}%where={zipcode}&tm={age}',
        'title_only_tempate': 'https://www.monster.com/jobs/search/?q={title}',
        'title_selector': '//section[{}]/div/div[2]/header/h2/a',
        'title_word_sep': '-',
        'body_selector': 'body'
    },
}

#todo: change below

SF_ZIPS = [95032,]
'''
             95054, 94010,
94536,

94539,
94402,
94404,
94403,
94538,
94560,
94065,
94063,
94027,
94002,
94070,
95134,
95002,
94062,
94089,
94301,
94025,
94303,
95035,
95140,
94061,
94043,
94304,
94305,
94035,
94306,
94028,
94040,
94022,
94085,
94086,
94024,
94087]
'''
