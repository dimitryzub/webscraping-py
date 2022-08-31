from bs4 import BeautifulSoup
import requests, lxml, os, json

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

proxies = {
  'http': os.getenv('HTTP_PROXY')
}

def get_profile_results_combo():
  html = requests.get('https://scholar.google.com/citations?view_op=view_org&hl=en&org=9834965952280547731', headers=headers, proxies=proxies).text

  soup = BeautifulSoup(html, 'lxml')

  author_ids = []

  for result in soup.select('.gs_ai_chpr'):
    name = result.select_one('.gs_ai_name a').text
    link = result.select_one('.gs_ai_name a')['href']
    # https://stackoverflow.com/a/6633693/15164646
    id = link
    id_identifer = 'user='
    before_keyword, keyword, after_keyword = id.partition(id_identifer)
    author_id = after_keyword
    affiliations = result.select_one('.gs_ai_aff').text
    email = result.select_one('.gs_ai_eml').text
    try:
      interests = result.select_one('.gs_ai_one_int').text
    except:
      interests = None
    cited_by = result.select_one('.gs_ai_cby').text.split(' ')[2]

    author_ids.append(author_id)
  print(author_ids)
  return author_ids


def get_author_results_combo(profiles):
  
  for id in profiles:
    html = requests.get(f'https://scholar.google.com/citations?hl=en&user={id}', headers=headers, proxies=proxies).text
    soup = BeautifulSoup(html, 'lxml')

    # Author info
    name = soup.select_one('#gsc_prf_in').text
    affiliation = soup.select_one('#gsc_prf_in+ .gsc_prf_il').text

    try:
      email = soup.select_one('#gsc_prf_ivh').text
    except:
      email = None

    try:
      interests = soup.select_one('#gsc_prf_int').text
    except:
      interests = None

    print('Author info:')
    print(f'{name}\n{affiliation}\n{email}\n{interests}\n')

    # Article info
    for article_info in soup.select('#gsc_a_b .gsc_a_t'):
      title = article_info.select_one('.gsc_a_at').text
      title_link = article_info.select_one('.gsc_a_at')['data-href']
      authors = article_info.select_one('.gsc_a_at+ .gs_gray').text
      publications = article_info.select_one('.gs_gray+ .gs_gray').text

      print('Article info:')
      print(f'Title: {title}\nTitle link: https://scholar.google.com{title_link}\Article Author(s): {authors}\Article Publication(s): {publications}\n')

    # Cited by and Public Access Info:
    for cited_by_public_access in soup.select('.gsc_rsb'):
      citations_all = cited_by_public_access.select_one('tr:nth-child(1) .gsc_rsb_sc1+ .gsc_rsb_std').text
      citations_since2016 = cited_by_public_access.select_one('tr:nth-child(1) .gsc_rsb_std+ .gsc_rsb_std').text
      h_index_all = cited_by_public_access.select_one('tr:nth-child(2) .gsc_rsb_sc1+ .gsc_rsb_std').text
      h_index_2016 = cited_by_public_access.select_one('tr:nth-child(2) .gsc_rsb_std+ .gsc_rsb_std').text
      i10_index_all = cited_by_public_access.select_one('tr~ tr+ tr .gsc_rsb_sc1+ .gsc_rsb_std').text
      i10_index_2016 = cited_by_public_access.select_one('tr~ tr+ tr .gsc_rsb_std+ .gsc_rsb_std').text
      articles_num = cited_by_public_access.select_one('.gsc_rsb_m_a:nth-child(1) span').text.split(' ')[0]
      articles_link = cited_by_public_access.select_one('#gsc_lwp_mndt_lnk')['href']
      
      print('Citiation info:')
      print(f'{citations_all}\n{citations_since2016}\n{h_index_all}\n{h_index_2016}\n{i10_index_all}\n{i10_index_2016}\n{articles_num}\nhttps://scholar.google.com{articles_link}\n')
      
      # Co-Authors
      try:
        for container in soup.select('.gsc_rsb_aa'):
          author_name = container.select_one('#gsc_rsb_co a').text
          author_affiliations = container.select_one('.gsc_rsb_a_ext').text
          author_link = container.select_one('#gsc_rsb_co a')['href']

          print('Co-Author(s):')
          print(f'{author_name}\n{author_affiliations}\nhttps://scholar.google.com{author_link}\n')
      except:
        pass

        # Graph results
        years = [graph_year.text for graph_year in soup.select('.gsc_g_t')]
        citations = [graph_citation.text for graph_citation in soup.select('.gsc_g_a')]
        
        data = []
        
        for year, citation in zip(years,citations):
          print(f'{year} {citation}\n')

          data.append({
            'year': year,
            'citation': citation,
          })

        # print(json.dumps(data, indent=2))
