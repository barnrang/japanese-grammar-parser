import pandas as pd
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()


df = {
    'link':[],
    'description':[],
    'level':[]
}
for i in range(1,10):
    status, response = http.request(f'https://jlptsensei.com/complete-jlpt-grammar-list/page/{i}/')

    soup = BeautifulSoup(response)

    all_grammars = soup.find_all("a", {"class": "jp jl-link"})
    all_levels = soup.find_all("td", {"class": "jl-td-nl"})
    for grammar, level in zip(all_grammars, all_levels):
        df['description'].append(grammar.string)
        df['link'].append(grammar['href'])
        df['level'].append(level.a.string)

pd.DataFrame(df).to_csv("grammars_list.csv", index=False)
