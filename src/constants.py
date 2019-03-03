SKILL_KEYWORDS_DEV =['python', 'c++', 'java', 'bash','ruby',
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
            'windows', 'C/C++', 'NVMe', 'SSD', 'HDD','Typescript' ]


SITES_DICT = {
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

        'careerbuilder': {
            'url_template': 'https://www.careerbuilder.com/jobs-{cbtitle}-in-{zipcode}?keywords={title}&location={zipcode}&radius={radius}&pay={salary}&posted={age}&',
            'title_selector': "//h2[@class='job-title show-for-medium-up']//a[@data-gtm='jrp-job-list|job-title-click|{}']",
            'title_word_sep': '+',
            'salaries': ['150', '100',  '50']

        },

        'indeed': {
            'url_template': 'https://www.indeed.com/jobs?as_and={title}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&st=&as_src=&salary={salary}&radius={radius}&l={zipcode}&fromage={age}&limit=500&sort=&psf=advsrch',
            'title_selector': 'turnstileLink',
            'title_word_sep': '+',
            'salaries': ['150000', '100000' ,'50000'],
        },

}

GEO_ZIPS = {

    'Sufolk County, Boston MA':
    [2101,
2102,
2103,
2104,
2105,
2106,
2107,
2108,
2109,
2110,
2111,
2112,
2113,
2114,
2115,
2116,
2117,
2118,
2118,
2119,
2119,
2120,
2121,
2122,
2123,
2124,
2125,
2126,
2127,
2128,
2129,
2130,
2131,
2132,
2133,
2134,
2135,
2136,
2137],



}





TITLES = {
    'software quality assurance engineer': [{'software': 50, 'quality': 60, 'assurance': 30, 'qa': 80, 'sqa': 90, 'sdet': 100, 'test': 50, 'automation': 30, 'automated': 30, 'engineer': 20, 'testing': 70},
     SKILL_KEYWORDS_DEV, True],
     #'data science engineer': [{'data':60, 'science':30, 'engineer':30, 'scientist': 30, 'quantitative': 50, 'analyst':40}, SKILL_KEYWORDS_DEV],
}
'''
'Travis County, Austin TX':[78764,
78768,
78767,
78772,
78769,
78783,
78610,
78613,
78615,
78617,
78621,
73301,
73344,
78641,
78645,
78652,
78654,
78653,
78660,
78664,
78669,
78691,
78702,
78701,
78704,
78703,
78705,
78712,
78713,
78716,
78719,
78722,
78721,
78724,
78723,
78726,
78725,
78728,
78727,
78730,
78732,
78731,
78734,
78733,
78736,
78735,
78738,
78737,
78741,
78739,
78744,
78742,
78746,
78745,
78748,
78747,
78750,
78749,
78752,
78751,
78754,
78753,
78756,
78758,
78757,
78760,
78759,],

'San Francisco Bay Area':
    [95032, 95054, 94010, 94536, 94539, 94402, 94404, 95054, 94010, 94536, 94539, 94402, 94404,
    94403, 94538, 94560, 94065, 94063, 94027, 94002,
    94070, 95134, 95002, 94062, 94089, 94301, 94025, 94303,
    95035, 95140, 94061, 94043, 94304, 94305, 94035, 94306, 94028, 94040, 94022, 94085, 94086,
    94024, 94087],
'''
