USE youtube_db;

--Create view from table
CREATE VIEW view_peru_youtubers_2024 AS
SELECT 
	CAST(TRIM(SUBSTRING(NAME,1,CHARINDEX('@', NAME) - 1)) AS varchar(100)) as channel_name,
	total_subscribers,
	total_views,
	total_videos
FROM	top_peru_youtubers_2024


--Check number of rows.
SELECT
	COUNT(*) 
FROM	view_peru_youtubers_2024


--Check number of columns.
SELECT
	COUNT(*) column_count
FROM	INFORMATION_SCHEMA.COLUMNS
WHERE	TABLE_NAME = 'view_peru_youtubers_2024'

	
--Check data types.
SELECT *
FROM	INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'view_peru_youtubers_2024'


--Check for duplicates.
SELECT 
	channel_name,
	COUNT(*) total
FROM	view_peru_youtubers_2024
GROUP BY channel_name
HAVING COUNT(*) > 1