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


'''
//*[@id="jl_f1d37e69b35a1bb9"]/a
//*[@id="jl_2933e681f94ba751"]/a
/html[1]/body[1]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[8]/h2[1]/a[1] 
/html[1]/body[1]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[{}]/h2[1]/a[1]

<a href="/company/Marpo-Kinetics/jobs/Design-Manufacturing-Engineer-08a3f281cecce90a?fccid=a81d4ba8cc0d6bf6&amp;vjs=3" 
target="_blank"
 rel="noopener nofollow" onmousedown="return rclk(this,jobmap[2],1);" 
 onclick="setRefineByCookie([]); return rclk(this,jobmap[2],true,1);" 
 title="Design/Manufacturing Engineer" 
 class="turnstileLink" 
 data-tn-element="jobTitle" xpath="1">Design/Manufacturing <b>Engineer</b></a>

'''