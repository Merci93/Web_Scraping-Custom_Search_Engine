import requests as rq
import pandas as pd

# import excel file containing links
link_list = pd.read_excel('CSE_links.xlsx')

# Create in google developer API
API_KEY = '*************************'

# Search Engine ID: already in the links
SEARCH_ENGINE_ID = '13269e598159c491e'

# List to hold extracted data
df_list = []

#iterate through links in the list:
for row in link_list['url']:
    query = row.split('=')[3]
    
    # iterate through the 10 pages in each link
    for page in range(1, 11):
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}"
        data = rq.get(url).json()
        search_items = data.get('items')

        # iterate through each page to get required data
        for i, search_item in enumerate(search_items):
            title = search_item.get("title")
            description = search_item.get("snippet")
            link = search_item.get("link")

            # append extracted data to list
            df_list.append({'company_name': title,
                            'url': link,
                            'description': description})

# convert results to a dataframe
df = pd.DataFrame(df_list, columns = ['company_name', 'url', 'description'])
    
# save file as CSV
df.to_csv('search_results.csv', index = False)
