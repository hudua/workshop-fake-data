
CREATE EXTERNAL DATA SOURCE Experimentation
WITH (
    LOCATION = 'abfss://experimentation@<storage-name>.dfs.core.windows.net/'
);



CREATE EXTERNAL FILE FORMAT CsvFormat
WITH (
    FORMAT_TYPE = DELIMITEDTEXT,
    FORMAT_OPTIONS (
        FIELD_TERMINATOR = ',',
        STRING_DELIMITER = '"',
        FIRST_ROW = 2
    )
);
