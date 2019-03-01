SKILL_KEYWORDS_QA =['python', 'c++', 'java', 'bash','ruby', ]


SITES_DICT = {
        'careerbuilder': {
            'url_template': 'https://www.careerbuilder.com/jobs-{cbtitle}-in-{zipcode}?keywords={title}&location={zipcode}&radius={radius}&pay={salary}&posted={age}&',
            'title_selector': "//h2[@class='job-title show-for-medium-up']//a[@data-gtm='jrp-job-list|job-title-click|{}']",
            'title_word_sep': '+',
            'salaries': ['150', '100',  '50']

        },
        'stackoverflow': {
            'url_template': 'https://stackoverflow.com/jobs?q={title}&l={zipcode}&d={radius}&u=Miles&s={salary}&c=USD&',
            'title_selector': 's-link',
            'title_word_sep': '+',
            'salaries': ['150000', '100000', '50000']
        },

}

GEO_ZIPS = {
    'San Francisco Bay Area':
        [95032, 95054, 94010,]

}


    #'Austin, Texas': [],
    #'Boston, Mass':[],
    #'New York, New York':[],
    #'Seattle, WA':[],




TITLES = {
    'software quality assurance engineer': [{'software': 50, 'quality': 60, 'assurance': 30, 'qa': 80, 'sqa': 90, 'sdet': 100, 'test': 60, 'automation': 30, 'automated': 30, 'engineer': 20, 'testing': 70},
     SKILL_KEYWORDS_QA],
    #'data science engineer': [{'data':60, 'science':30, 'engineer':30, 'scientist': 30, 'quantitative': 50, 'analyst':40}], SKILL_KEYWORDS_QA],

}


'''

'perl', 'matlab', 'javascript', 'scala', 'firmware', 'Machine', ' Espresso', 'learning', 'map', 'reduce', 'big','ec2', 'warehouse', 'statistical', 'visualizations', 'visualization',
                 'php', 'Sauce Labs', 'flask', 'shell', 'solaris', 'Telecom', 'NAS', 'iSCSI', 'scripts', 'scripting','ETL', 'Collibra', 'OneData',
                 'junit', 'selenium', 'react', 'c#', 'TestRail', 'Confluence', 'JMeter', 'Vertica', 'Logstash', 'Kibana',
                'tableau', 'd3.js', 'sas', 'spss', 'd3', 'saas', 'pandas', 'numpy', 'Jenkins', 'scipy', 'plan', 'case',
                'sps', 'spotfire', 'scikits.learn', 'splunk', 'h2o', 'jira', 'functional', 'integration', 'stress', 'load','performance',
                'hadoop', 'mapreduce', 'spark', 'pig', 'hive', 'shark', 'oozie', 'zookeeper', 'flume', 'mahout', 'bi'
                'elasticsearch', 'api', 'apis', 'Mockito', 'Robotium', 'frontend', 'backend', 'Informatica', 'Julia',
              'sql', 'nosql', 'hbase', 'cassandra', 'xml', 'rust', 'mongodb', 'mysql', 'mssql', 'postgre', 'oracle',
             'rdbms', 'mobile', 'android', 'ios', 'cucumber', 'iot', 'black', 'white', 'telecommunications', 'Superset', 'ggplot',
             'hive', 'cucumber', 'aws', 'azure', 'amazon', 'google', 'rest', 'docker', 'container', 'puppet', 'chef',
             'kubernetes', 'storage', 'network', 'networking', 'maven', 'ci', 'cd', 'ci/cd', 'gui', 'marketing', 'MDM', 'PL/SQL',
            'restassured', 'ios', 'json', 'swift', 'objective-c', 'groovy', '.net', 'angular', 'node.js', 'kafka', 'mesos','go',
            'django', 'pytest', 'css', 'html', 'appium', 'linux', 'css', 'ui', 'soa', 'unix', 'RESTful', 'Elastic', 'git',
            'github', 'database', 'acceptance', 'uat', 'healthcare', 'banking', 'Excel', 'r', 'Statistics', 'Mathematics','SparkSQL',
            'Druid', 'Solr','Economics', 'clickstream', 'Haskell', 'nomad', 'nix', 'bazil', 'buck', 'key-value','NLP', 'Bayesian', 'Gurobi',
            'windows', 'C/C++', 'NVMe', 'SSD', 'HDD', ]


94536, 94539, 94402, 94404, 95054, 94010, 94536, 94539, 94402, 94404,
94403, 94538, 94560, 94065, 94063, 94027, 94002,
94070, 95134, 95002, 94062, 94089, 94301, 94025, 94303,
95035, 95140, 94061, 94043, 94304, 94305, 94035, 94306, 94028, 94040, 94022, 94085, 94086,
94024, 94087],


    'stackoverflow': {
        'url_template': 'https://stackoverflow.com/jobs?q={title}&l={zipcode}&d={radius}&u=Miles&s={salary}&c=USD&',
        'title_selector': 's-link',
        'title_word_sep': '+',
        'salaries': ['150000', '100000', '50000']
    },

    'ziprecruiter': {
        'url_template': 'https://www.ziprecruiter.com/candidate/search?search={title}&location={zipcode}&days={age}&radius={radius}&refine_by_salary={salary}&',
        'title_selector': 'job_link',
        'title_word_sep': '+',
        'salaries': ['150000', '100000', '50000']

    },

    'indeed': {
        'url_template': 'https://www.indeed.com/jobs?as_and={title}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&st=&as_src=&salary={salary}&radius={radius}&l={zipcode}&fromage={age}&limit=500&sort=&psf=advsrch',
        'title_selector': 'turnstileLink',
        'title_word_sep': '+',
        'salaries': ['150000', '100000' ,'50000'],
    },

'''
