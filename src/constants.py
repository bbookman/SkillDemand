SUPERFLOUS_STRINGS = ['senior', 'director', 'manager', 'lead', 'mobile', 'sr', 'jr', 'I', 'II', 'III', 'IV','V' ,'(', ')', '.', ',', '/', '\\', "\'", '\"', '-',]

SITES_DICT = {

    indeed: {
        'url_template' : 'https://www.indeed.com/jobs?as_and={title}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&st=&as_src=&salary={salary}&radius={radius}&l={zipcode}fromage={age}&limit=500&sort=&psf=advsrch',
        'title_only_tempate': 'https://www.indeed.com/q-{}.html',
        'xpath_template' : '//*[@id="sja{}"]',
        'title_xpath': '/html/body/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/div[1]/h3'
        'title_finder' : 'as_and=',
        'title_word_sep': '+',
    },
# https://www.monster.com/jobs/search/Full-Time_8?q=technical-support-engineer&intcid=skr_navigation_nhpso_searchMain&rad=30&where=Santa-Clara__2c-CA&tm=30

    monster: {
        'url_template' : '# https://www.monster.com/jobs/search/Full-Time_8?q={}&rad={}&where={}&tm={}' #tm is age
        'title_only_tempate': 'https://www.monster.com/jobs/search/?q={}',
        'jd_link_finders' : #NOT APPLICABLE WITHOUT FIX ISSUE #20
        'title_finder' : 'q=',
        'title_word_sep': '-',
    },

    '''
    <a data-bypass="true" href="https://job-openings.monster.com/technical-support-engineer-santa-clara-ca-us-ledgent/d87787fa-6de7-4d01-92c1-45586c94b97d"
     onmousedown="dataLayer.push({'eventCategory':'LPF Job Listing','eventAction':'Title Link Click',
     'eventLabel':'2'});; clickJobTitle('plid=356&amp;pcid=660&amp;poccid=11969',
     'technical support engineer',''); " rel="nofollow" coretrack="{&quot;olduuid&quot;:&quot;b1977f98-9dcf-49ad-a014-f811a46f65c4&quot;,
     &quot;s_t&quot;:&quot;t&quot;,&quot;j_jobid&quot;:&quot;0&quot;,&quot;j_postingid&quot;:&quot;d87787fa-6de7-4d01-92c1-45586c94b97d&quot;,
     &quot;j_jawsid&quot;:&quot;360628550&quot;,&quot;j_pvc&quot;:&quot;jobcomftpin&quot;,&quot;j_coc&quot;:&quot;-1&quot;,&quot;j_cid&quot;
     :&quot;660&quot;,&quot;j_occid&quot;:&quot;11969&quot;,&quot;j_lid&quot;:&quot;356&quot;,&quot;j_p&quot;:&quot;2&quot;,&quot;
     j_lat&quot;:&quot;37.3934&quot;,&quot;j_long&quot;:&quot;-121.9655&quot;,&quot;j_jpt&quot;:&quot;2&quot;,&quot;j_jpm&quot;:&quot;1&quot;,&quot;j_placementid&quot;
     :&quot;JSR2CW&quot;,&quot;s_search_query&quot;:&quot;q%3Dtechnical%2520support%2520engineer%26brd%3D1%26brd%3D2%26cy%
     3DUS%26pp%3D25%26sort%3Drv.di.dt%26nosal%3Dtrue%26geo%3DSanta%252520Clara%25252c%252520CA%252c48.28032%252c1273541%2
     52c580447%252c356%252cCity%26stp%3DScoreFenceMain&quot;,&quot;s_q&quot;:&quot;Technical%20Support%20Engineer&quot;,&quot;
     s_where&quot;:&quot;Santa%20Clara&quot;,&quot;j_pg&quot;:&quot;1&quot;,&quot;a_affiliate_id&quot;:&quot;Monster&quot;
     ,&quot;uinfo&quot;:&quot;-1&quot;,&quot;isloggedin&quot;:&quot;False&quot;,&quot;uuid&quot;:&quot;
     0c52ebb8-a29a-4b3e-8657-f48b3368f6c8&quot;}" coretrackclickadded="true">Technical Support Engineer</a>
</a>
    '''

    dice: {
        'url_template' :
        'title_only_tempate':
        'jd_link_finders' :
        'title_finder' :
        'title_word_sep':
    },

    careerbuilder: {
        'url_template' :
        'title_only_tempate':
        'jd_link_finders' :
        'title_finder' :
        'title_word_sep':
    },

}


'''
_URL_TEMPATE

'''
