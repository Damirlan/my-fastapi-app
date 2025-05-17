ATTACH TABLE _ UUID '57ebc7da-5a61-42a4-9be9-40be2c51067e'
(
    `timestamp` DateTime,
    `severity` String,
    `body` String,
    `attributes` Map(String, String)
)
ENGINE = MergeTree
ORDER BY timestamp
SETTINGS index_granularity = 8192
