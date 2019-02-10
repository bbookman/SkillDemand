SUPERFLOUS_STRINGS = ['senior', 'director', 'manager', 'lead', 'mobile', 'sr', 'jr', 'I', 'II', 'III', 'IV','V' ,'(', ')', '.', ',', '/', '\\', "\'", '\"', '-',]

INDEED_URL_TEMPATE = 'https://www.indeed.com/jobs?as_and={}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt={}&st=&as_src=&salary={}&radius={}&l={}fromage={}&limit=500&sort=&psf=advsrch'
# https://www.indeed.com/jobs?as_and=senior+technical+support+engineer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=fulltime&st=&as_src=&salary=145000&radius=100&l=San+Jose,+CA&fromage=300&limit=50&sort=&psf=advsrch
INDEED_TITLE_ONLY_TEMPLATE = 'https://www.indeed.com/q-{}.html' #dash separated title text such as data-science-engineer
INDEED_JD_LINK_FINDERS = ['a', "jobtitle turnstileLink"] #for parse_site_for_jd_links(url, link_finders)
INDEED_TITLE_FINDER = 'as_and=' #for get_related_titles
INDEED_TITLE_WORD_SEP = '+'
