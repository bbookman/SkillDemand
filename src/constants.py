SUPERFLOUS_STRINGS = ['senior', 'director', 'manager', 'lead', 'mobile', 'sr', 'jr', 'I', 'II', 'III', 'IV','V' ,'(', ')', '.', ',', '/', '\\', "\'", '\"', '-',]

SITES_DICT = {

    'indeed': {
        'url_template' : 'https://www.indeed.com/jobs?as_and={title}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&st=&as_src=&salary={salary}&radius={radius}&l={zipcode}&fromage={age}&limit=500&sort=&psf=advsrch',
        'title_only_tempate': 'https://www.indeed.com/q-{}.html',
        'xpath_template' : '//*[@id="sja{}"]',
        'title_word_sep': '+',
        'body_selector': 'body'
    },
    'monster':{
        'url_template' : 'https://www.monster.com/jobs/search/?q={title}&rad={radius}%where={zipcode}&tm={age}',
        'title_only_tempate': 'https://www.monster.com/jobs/search/?q={title}',
        'xpath_template': '//section[{}]/div/div[2]/header/h2/a',
        'title_word_sep': '-',
        'body_selector': 'body'
    },
}
