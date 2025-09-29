-- This is auto-generated code
SELECT
    y.ProgramID, ProgramName, ApplicationCost
FROM
    OPENROWSET(
        BULK 'https://<storage-name>.dfs.core.windows.net/experimentation/data/fsspec/program_costs.csv',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',
        HEADER_ROW = TRUE
    ) AS [result]

join dbo.social_programs y on [result].ProgramID = y.ProgramID
