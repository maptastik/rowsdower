#!/usr/bin/env python
# coding: utf-8

import os
from datetime import datetime
import csv
from arcgis.gis import GIS

def rowsdower(portal, username, password, item_id, table_name, field, count):
    gis = GIS(portal, username, password)
    print(f'Logged in as {gis.properties.user.username}.')

    # Get table
    table_search = gis.content.get(item_id)
    tables = table_search.tables

    for table in tables:
        if table.properties['name'] == table_name:
            target_table = table

    # Create a temporary CSV
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    temp_csv_name = f'temp_{now}.csv'
    temp_csv_path = os.path.join(os.getcwd(), temp_csv_name)

    header = [field]
    csvdata = [['New Row'] for n in range(count)]
    with open(temp_csv_path, 'w', newline = '') as temp_csv:
        writer = csv.writer(temp_csv, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(i for i in header)
        writer.writerows(csvdata)

    temp_item_properties = {"title":"new_table_row_temp",
                    "type":"CSV",
                    "tags":"temp",
                    "snippet":"Temporary CSV item for adding new rows to a standalone table",
                    "description":"Temporary CSV item for adding new rows to a standalone table"}
    temp_item = gis.content.add(item_properties = temp_item_properties, data = temp_csv_path)

    temp_item_source_info = gis.content.analyze(item = temp_item.id, file_type = 'csv', location_type = 'none')
    target_table.append(item_id = temp_item.id,
                upload_format = 'csv',
                source_info = temp_item_source_info['publishParameters'],
                update_geometry = False,
                upsert = False,
                append_fields = [field])

    temp_item = gis.content.get(temp_item.id)
    temp_item.delete()

    os.remove(temp_csv_path)
    print("complete")