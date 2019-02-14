SUPERFLOUS_STRINGS = ['senior', 'director', 'manager', 'lead', 'mobile', 'sr', 'jr', 'I', 'II', 'III', 'IV','V' ,'(', ')', '.', ',', '/', '\\', "\'", '\"', '-',]



SITES_DICT = {

    'indeed' :{
        'url_template' : 'https://www.indeed.com/jobs?as_and={title}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&st=&as_src=&salary={salary}&radius={radius}&l={zipcode}&fromage={age}&limit=500&sort=&psf=advsrch',
        'title_only_template': 'https://www.indeed.com/q-{}.html',
        'title_selector' : 'turnstileLink',
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

SF_ZIPS = [95032,

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
