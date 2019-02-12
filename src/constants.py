SUPERFLOUS_STRINGS = ['senior', 'director', 'manager', 'lead', 'mobile', 'sr', 'jr', 'I', 'II', 'III', 'IV','V' ,'(', ')', '.', ',', '/', '\\', "\'", '\"', '-',]

SITES_DICT = {

    indeed: {
        'url_template' : 'https://www.indeed.com/jobs?as_and={title}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&st=&as_src=&salary={salary}&radius={radius}&l={zipcode}fromage={age}&limit=500&sort=&psf=advsrch',
        'title_only_tempate': 'https://www.indeed.com/q-{}.html',
        'xpath_template' : '//*[@id="sja{}"]',
        'title_word_sep': '+',
    },
# https://www.monster.com/jobs/search/Full-Time_8?q=technical-support-engineer&intcid=skr_navigation_nhpso_searchMain&rad=30&where=Santa-Clara__2c-CA&tm=30

    monster: {
        'url_template' : '# https://www.monster.com/jobs/search/Full-Time_8?q={}&rad={}&where={}&tm={}' #tm is age
        'title_only_tempate': 'https://www.monster.com/jobs/search/?q={}',
        'jd_link_finders' : #NOT APPLICABLE WITHOUT FIX ISSUE #20
        'title_word_sep': '-',
    },


    dice: {
        'url_template' :
        'title_only_tempate':
        'jd_link_finders' :
        'title_word_sep':
    },

    careerbuilder: {
        'url_template' :
        'title_only_tempate':
        'jd_link_finders' :
        'title_word_sep':
    },

}


'''
_URL_TEMPATE

'''
