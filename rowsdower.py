#!/usr/bin/env python
# coding: utf-8

# # rowsdower exploration
# 
# The goal here is to work out the logic for a simple too that adds 1+ new rows to a standalone table in ArcGIS Online

# In[ ]:


from getpass import getpass
from pprint import pprint
from IPython.display import display

import os
from datetime import datetime
import csv

from arcgis.gis import GIS


# ## Login to AGOL

# In[ ]:


portal = 'https://ral.maps.arcgis.com'
user = 'RaleighPRCR'
password = getpass()
gis = GIS(portal, user, password)
print(f'Logged in as {gis.properties.user.username}.')


# # Gather item to update information

# In[ ]:


item_id = 'da7ab59d8303415b91d520f417d83537'
table_name = 'table_1'
template_field = 'NAME'
new_row_count = 2


# ## Get table

# In[ ]:


table_search = gis.content.get(item_id)
tables = table_search.tables

for table in tables:
    if table.properties['name'] == table_name:
        target_table = table
        
print(target_table)


# ## Create a temporary CSV

# In[ ]:


now = datetime.now().strftime('%Y%m%d%H%M%S')
temp_csv_name = f'temp_{now}.csv'
temp_csv_path = os.path.join(os.getcwd(), temp_csv_name)

header = [template_field]
csvdata = [['New Row'] for n in range(new_row_count)]
with open(temp_csv_path, 'w', newline = '') as temp_csv:
    writer = csv.writer(temp_csv, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(i for i in header)
    writer.writerows(csvdata)


# In[ ]:


temp_item_properties = {"title":"new_table_row_temp",
                   "type":"CSV",
                   "tags":"temp",
                   "snippet":"Temporary CSV item for adding new rows to a standalone table",
                   "description":"Temporary CSV item for adding new rows to a standalone table"}
temp_item = gis.content.add(item_properties = temp_item_properties, data = temp_csv_path)


# In[ ]:


temp_item_source_info = gis.content.analyze(item = temp_item.id, file_type = 'csv', location_type = 'none')
target_table.append(item_id = temp_item.id,
               upload_format = 'csv',
               source_info = temp_item_source_info['publishParameters'],
               update_geometry = False,
               upsert = False,
               append_fields = [template_field])


# In[ ]:


temp_item = gis.content.get(temp_item.id)
temp_item.delete()

os.remove(temp_csv_path)

