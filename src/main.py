import ssl, pdb
import copy
import logging
from constants import *
from utility import *



logging.basicConfig(filename='execution_{date}.log'.format(date = make_date_string()), level=logging.INFO)
ssl._create_default_https_context = ssl._create_unverified_context


if __name__ == "__main__":
    start = make_time_string()
    skill_summary = dict()
    salaries = dict()
    zcode = dict()
    area = dict()
    titles = dict()

    for site_id in SITES_DICT.keys():
        stime = make_time_string()
        print(f'PROGREAM START {stime} ')
        logging.info(f'START {site_id}: {stime} ')
        title_separator = SITES_DICT[site_id]['title_word_sep']
        title_selector = SITES_DICT[site_id]['title_selector']
        site_url_template = SITES_DICT[site_id]['url_template']
        for title in TITLES.keys():
            skip_dups = TITLES[title][2]
            skill_keywords = TITLES[title][1]
            weights = TITLES[title][0]
            titles.setdefault(title, 'DEFAULT TITLE')
            for geo in GEO_ZIPS.keys():
                time = make_time_string()
                print(f'PROGREAM START WAS {site_id}: {stime} ')
                print(f'START GEO:{geo}: {time} ')
                logging.info(f'START GEO:{geo}: {time} ')
                for salary in SITES_DICT[site_id]['salaries']:
                    time = make_time_string()
                    print(f'START SALARY:{salary}: {time} ')
                    logging.info(f'START SALARY:{salary}: {time} ')
                    if site_id =='careerbuilder':
                        salaries.setdefault(salary+'000', dict())
                    else:
                        salaries.setdefault(salary, dict())
                    for zip in GEO_ZIPS[geo]:
                        print(f'zip:{zip}')
                        zip = str(zip)
                        zcode.setdefault(zip, dict())
                        skill_counts = dict()
                        skill_counts = get_skills(skip_dups, geo, skill_counts, site_id, site_url_template, title, title_separator, title_selector, salary, skill_keywords, weights, zip,)
                        for skill, value in skill_counts.items():
                            skill_summary.setdefault(skill,0)
                            skill_summary[skill] += value
                        cp = copy.deepcopy(skill_summary)
                        for k, v in cp.items():
                            if v == 0:
                                skill_summary.pop(k)
                        zcode[zip] = skill_summary
                    if site_id == 'careerbuilder' and len(salary)<=3:
                        salary+= '000'
                    salaries[salary] = zcode
                area[geo] = salaries
                print(f'END GEO: {geo}: {time}')
                logging.info(f'END GEO: {geo}: {time}')
                gs = geo.split()
                g = ''
                for word in gs:
                    g+=word+'_'
                with open(f'{g}_{t}_RESULTS.txt', 'w') as file:
                    file.write(str(area))
                    file.close()
            titles[title] = area
            time = make_time_string()
            print(f'END TITLE {title}: {time}')
            logging.info(f'END TITLE {title}: {time}')
        time = make_time_string()
        print(f'END {site_id}: {time} ')
        logging.info(f'END {site_id}: {time} ')


    print(f'PROGRAM START TIME:{stime}')
    logging.info(f'PROGRAM START TIME:{stime}')
    end = make_time_string()
    print(f'PROGRAM END TIME:{end}')
    logging.info(f'PROGRAM END TIME:{end}')

with open(f'{title}_{geo}_RESULTS.txt', 'w') as file:
    file.write(str(titles))
    file.close()
