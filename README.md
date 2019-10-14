# rowsdower

rowsdower is simple Python tool for doing one thing: adding some new rows to a table in an ArcGIS Online Hosted Feature Service. Currently adding a new row to a table is cumbersome, particularly if you have a feature service containing only tables. Currently, the only ways to add a new row to a table are:

- Create a local file (e.g. CSV, JSON) with the same schema as the table, populate the values, and upload the result as a part of the Append operation in the AGOL GUI.
- Add the table to a map in ArcGIS Pro, open it as an attribute table, and add a new row.
- Do something programmatic.

What you can't do:

- Create a new row from within the table's data tab in AGOL.
- Create a new row from within AGOL's map interface.
- Create a Survey123 survey based on a feature service containing tables only.

This project is meant to provide a lighter-weight, less cumbersome means to adding new, blank rows to a table. It is not meant to provide a a form for filling out new row values. Rather, it should create the rows such that you can then go into AGOL and add the appropriate attribute values through the AGOL web interface.
